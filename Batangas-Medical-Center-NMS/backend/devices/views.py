from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Devices
from .serializers import DeviceSerializer
from scapy.all import ARP, Ether, srp
from rest_framework import status
from ping3 import ping
import time
from .email_module import send_email

@api_view(['GET'])
def send_test_email(request):
    subject = "Alert Device"
    body = "This Device is down. here are the details."
    sender = "andreaf.fifibuy@gmail.com"
    recipients = ["yahjihyoo@gmail.com", ]
    password = "mysy bhty ijhx tcat" #"zogt bmje dmbg vivf"
    # mysy bhty ijhx tcat fifibuy


    send_email(subject, body, sender, recipients, password)
    return  Response({'message': 'Email completed successfully.'})

@api_view(['POST'])
def scan_devices(request):
    target_ip = request.data.get('target_ip')

    # Scanning process
    try:
        # Create an ARP request packet
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        # Send the packet and capture the response
        result = srp(packet, timeout=3, verbose=0)[0]

        # Update or create devices based on the response
        for sent, received in result:
            Devices.objects.update_or_create(
                ip_address=received.psrc,
                defaults={'mac_address': received.hwsrc}
            )

        # Perform network scan and update device status
        update_device_status()

        return Response({'message': 'Scan completed successfully.'})
    except Exception as e:
        return Response({'message': f'Error scanning devices: {str(e)}'})


def scan_devices_ver2(request):
    target_ip = request.data.get('target_ip')

    # Scanning process
    try:
        # Create an ARP request packet
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        # Send the packet and capture the response
        result = srp(packet, timeout=5, verbose=0)[0]

        # Update or create devices based on the response
        for sent, received in result:
            Devices.objects.update_or_create(
                ip_address=received.psrc,
                defaults={'mac_address': received.hwsrc}
            )

        # Perform network scan and update device status
        update_device_status()

        return Response({'message': 'Scan completed successfully.'})
    except Exception as e:
        return Response({'message': f'Error scanning devices: {str(e)}'})

@api_view(['GET'])
def get_scanned_devices(request):

    # Retrieve the list of devices from the database
    devices = Devices.objects.all()

    # Perform network scan and update device status
    update_device_status()

    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


def update_device_status():
    devices = Devices.objects.all()

    for device in devices:
        # Print the device IP address for debugging
        print('Checking device:', device.ip_address)

        # Perform a ping request to check the device's availability
        response_time = ping(device.ip_address)

        # Check the response to determine the device status
        if isinstance(response_time,float):
            # Device is active
            device.status = 'active'
        else:
            # Device is down or inactive
            device.status = 'down'
            subject = "Alert Device"
            body = "Down Device Notification. Here are the details about it: \n\n\n"
            body += f"Device ID: {device.deviceId}\n"
            body += f"Device Name: {device.deviceName}\n"
            body += f"Device Type: {device.deviceType}\n"
            body += f"Device Status: {device.status}\n"
            body += f"Department: {device.department}\n"
            body += f"Buiding: {device.building}\n"
            body += f"Floor {device.floor}\n"
            body += f"IP Address: {device.ip_address}\n"
            body += f"MAC Address: {device.mac_address}\n"


            sender = "andreaf.fifibuy@gmail.com"
            recipients = ["yahjihyoo@gmail.com", ]
            password = "mysy bhty ijhx tcat" #"zogt bmje dmbg vivf"
            # mysy bhty ijhx tcat fifibuy
            send_email(subject, body, sender, recipients, password)

        time.sleep(0.5)
        print(response_time)
        # Save the updated device status to the database
        device.save()


@api_view(['GET'])
def get_scanned_device(request, device_id):
    try:
        devices = Devices.objects.get(deviceId=device_id)

        # Perform network scan and update device status
        update_device_status()

        serializer = DeviceSerializer(devices)
        return Response(serializer.data)
    except Devices.DoesNotExist:
        return Response({'message': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_scanned_device(request, device_id):
    try:
        devices = Devices.objects.get(deviceId=device_id)
        serializer = DeviceSerializer(devices, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Perform network scan and update device status
            update_device_status()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Devices.DoesNotExist:
        return Response({'message': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_scanned_device(request, device_id):
    try:
        devices = Devices.objects.get(deviceId=device_id)
        devices.delete()

        # Perform network scan and update device status
        update_device_status()

        return Response({'message': 'Device deleted successfully.'})
    except Devices.DoesNotExist:
        return Response({'message': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)