from scapy.all import ARP, Ether, srp
from .models import Devices


def perform_network_scan(target_ip):
    # Create an ARP request packet to get the MAC addresses of devices in the network
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Extract the IP and MAC addresses from the response
    devices = []
    for sent, received in result:
        ip_address = received.psrc
        mac_address = received.hwsrc

        # Fetch additional variables from Devices model using IP address
        try:
            device, created = Devices.objects.get_or_create(ip_address=ip_address, defaults={
                'deviceName': None,
                'deviceType': None,
                'building': None,
                'floor': None,
                'department': None,
            })

            # Update the fields of an existing device
            if not created:
                device.deviceName = None
                device.deviceType = None
                device.building = None
                device.floor = None
                device.department = None

            device.save()

            devices.append({
                'ip_address': ip_address,
                'mac_address': mac_address,
                'device_name': device.deviceName,
                'device_type': device.deviceType,
                'building': device.building,
                'floor': device.floor,
                'department': device.department,
            })

        except Devices.DoesNotExist:
            devices.append({
                'ip_address': ip_address,
                'mac_address': mac_address,
                'device_name': None,
                'device_type': None,
                'building': None,
                'floor': None,
                'department': None,
            })

    return devices