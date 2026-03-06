from rest_framework import serializers
from station.models import Bus

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


class BusSerializer(serializers.ModelSerializer):
    is_small = serializers.BooleanField()
    class Meta:
        model = Bus
        fields = "__all__"




