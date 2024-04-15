from rest_framework import serializers
from .models import Devices

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['deviceId',
                  'deviceName',
                  'ip_address',
                  'mac_address',
                  'deviceType',
                  'building',
                  'floor',
                  'department',
                  'status',
                  ]