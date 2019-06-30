from django.urls import include, path
from . import views
from django.views.generic.base import RedirectView
from devices.apis import apis

# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'devices'

# ToDo: 端末名に"-"が入っていると動作しない??
urlpatterns = [
    #### 端末のロケーション（緯度、経度）データ
    path('api/v1.0/devices/<str:smartphoneID>/locations/', apis.devices_locations.as_view(), name='apis_devices_locations'),

    ##### 道路損傷データ
    path('api/v1.0/devices/<str:smartphoneID>/damages/',  apis.devices_damages.as_view(), name='apis_devices_damages'),

    ### アプリケーション
    path('api/v1.0/app/version/', apis.devices_app_version.as_view(), name='apis_devices_app_version'),
    path('api/v1.0/app/download/', apis.devices_app_download.as_view(), name='apis_devices_app_download'),
]
