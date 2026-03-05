from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

from station.models import Bus
from station.serializers import BusSerializer

'''
'''


# Function base views. You can get access to this features form url path before FBV/
@api_view(["GET", "POST"])
def bus_list(request):
    if request.method == "GET":
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "DELETE"])
def bus_detail(request, pk: int):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == "GET":
        serializer = BusSerializer(bus)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = BusSerializer(bus, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class base views with APIView class. You can get access this features form url path before CBV/APIView/
class BusList(APIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request) -> Response:
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusDetail(APIView):

    def get_object(self, pk) -> Bus:
        return get_object_or_404(Bus, pk=pk)

    def get(self, request, pk) -> Response:
        serializer = BusSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk) -> Response:
        serializer = BusSerializer(self.get_object(pk=pk), data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk) -> Response:
        serializer = BusSerializer(self.get_object(pk=pk), data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) -> Response:
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class base views with GenericAPIView class. You can get access this
# features form url path before CBV/GMAPIV/
class BusListGM(
    generics.GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class BusDetailGM(
    generics.GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)


# Class base views with GenericView class. You can get access this
# features form url path before CBV/GV/
class BusListGV(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


# Class base views with GenericViewSet class. You can get access this
# features form url path before CBV/GVS/
class BusViewSet(
    viewsets.ModelViewSet,
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
