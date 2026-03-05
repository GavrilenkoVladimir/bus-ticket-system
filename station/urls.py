from django.urls import path

from station.views import (
    BusList,
    BusDetail,
    BusListGM,
    BusDetailGM,
    BusListGV,
    BusDetailGV,
    BusViewSet
)

app_name = "station"

bus_list = BusViewSet.as_view({
    "get": "list",
    "post": "create"
})
bus_detail = BusViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("FBV/buses/", bus_list, name="bus_list"),
    path("FBV/buses/<int:pk>", bus_detail, name="bus_detail"),
    path("CBV/APIV/buses/", BusList.as_view(), name="bus_list_apiview"),
    path("CBV/APIV/buses/<int:pk>/", BusDetail.as_view(), name="bus_detail_apiview"),
    path("CBV/GMAPIV/buses/", BusListGM.as_view(), name="bus_list_g_apiview"),
    path("CBV/GMAPIV/buses/<int:pk>/", BusDetailGM.as_view(), name="bus_detail_g_apiview"),
    path("CBV/GV/buses/", BusListGV.as_view(), name="bus_list_g_view"),
    path("CBV/GV/buses/<int:pk>/", BusDetailGV.as_view(), name="bus_detail_g_view"),
    path("CBV/GVS/buses/", bus_list, name="bus_list_g_view_set"),
    path("CBV/GVS/buses/<int:pk>/", bus_detail, name="bus_detail_g_view_set"),
]
