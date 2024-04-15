from django.db import models

class Devices(models.Model):
    deviceId = models. AutoField(primary_key=True)
    deviceName = models.CharField(max_length=100, blank=True, null=True, default='')
    ip_address = models.GenericIPAddressField(unique=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    deviceType = models.CharField(max_length=100, blank=True, null=True, default='')
    building = models.CharField(max_length=100, blank=True, null=True, default='')
    floor = models.CharField(max_length=100, blank=True, null=True, default='')
    department = models.CharField(max_length=100, blank=True, null=True, default='')
    status = models.CharField(max_length=10, default='unknown')