from django.urls import path
from .views import (scan_devices,
                    get_scanned_devices,
                    get_scanned_device,
                    update_scanned_device,
                    delete_scanned_device,
                    )

urlpatterns = [
    path('scan/', scan_devices, name='scan_devices'),
    path('scan/ver2/', scan_devices, name='scan_devices'),
    path('devices/scanned/', get_scanned_devices, name='get_scanned_devices'),
    path('devices/scanned/<int:device_id>/', get_scanned_device, name='get_scanned_device'),
    path('devices/scanned/<int:device_id>/update/', update_scanned_device, name='update_scanned_device'),
    path('devices/scanned/<int:device_id>/delete/', delete_scanned_device, name='delete_scanned_device'),
]
