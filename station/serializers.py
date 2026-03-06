from rest_framework import serializers
from station.models import Bus, Ticket, Trip, Order, Facility

'''
Representing a serializer using a model Serializer.
'''


# class BusSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     info = serializers.CharField(max_length=255, required=False)
#     num_seats = serializers.IntegerField(required=True)
#
#     def create(self, validated_data):
#         return Bus.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.info = validated_data.get("info", instance.info)
#         instance.num_seats = validated_data.get("num_seats", instance.num_seats)
#         instance.save()
#         return instance


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ("id", "name",)


class BusSerializer(serializers.ModelSerializer):
    is_small = serializers.ReadOnlyField()

    class Meta:
        model = Bus
        fields = ("id", "info", "num_seats", "is_small", "facility")


class BusListSerializer(BusSerializer):
    facility = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class BusRetrieveSerializer(BusSerializer):
    facility = FacilitySerializer(many=True)


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ("id", "source", "destination", "departure", "bus")


class TripListSerializer(serializers.ModelSerializer):
    bus_info = serializers.CharField(source="bus.info", read_only=True)
    bus_num_seats = serializers.IntegerField(source="bus.num_seats", read_only=True)

    class Meta:
        model = Trip
        fields = (
            "id",
            "source",
            "destination",
            "departure",
            "bus_info",
            "bus_num_seats"
        )


class TripRetrieveSerializer(TripSerializer):
    bus = BusListSerializer(many=False, read_only=True)