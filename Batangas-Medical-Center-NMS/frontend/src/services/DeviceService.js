import axios from 'axios';

export function getDevices() {
  return axios.get('http://127.0.0.1:8000/api/devices/scanned/')
    .then(response => response.data)
}

export function deleteDevice(deviceId, device) {
  return axios.delete('http://127.0.0.1:8000/api/devices/scanned/' + deviceId + '/delete/', {
   method: 'DELETE',
   headers: {
     'Accept':'application/json',
     'Content-Type':'application/json'
   }
  })
  .then(response => response.data)
}
export function addDevice(device){
  return axios.post('http://127.0.0.1:8000/api/devices/scanned/', {
    deviceId:null,
    deviceName:device.deviceName.value,
    ip_address:device.ip_address.value,
    mac_address:device.mac_address.value,
    deviceType:device.deviceType.value,
    building:device.building.value,
    floor:device.floor.value,
    department:device.department.value,
    status:null
  })
    .then(response=>response.data)
}
export function updateDevice(devid, device) {
  return axios.put('http://127.0.0.1:8000/api/devices/scanned/' + devid + '/update/', {
    deviceName:device.deviceName.value,
    ip_address:device.ip_address.value,
    mac_address:device.mac_address.value,
    deviceType:device.deviceType.value,
    building:device.building.value,
    floor:device.floor.value,
    department:device.department.value,
  })
   .then(response => response.data)
}