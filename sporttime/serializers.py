
from rest_framework import serializers
from sporttime.models import TurfDb, BookingDb


class Turf_serializer(serializers.ModelSerializer):
    class Meta:
        model=TurfDb
        fields="__all__"

        read_only_fields=["id"]


class Booking_serializer(serializers.ModelSerializer):
    class Meta:
        model=BookingDb
        fields="__all__"
        read_only_fields=["id"]
        
