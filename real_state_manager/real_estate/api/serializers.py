from rest_framework import serializers

from real_state_manager.real_estate.models import Property
from real_state_manager.real_estate.models import Reservation


class PropertySerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Property
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Reservation
        fields = "__all__"


class ReservationUpdateSerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Reservation
        fields = [
            "renting_price",
            "number_of_guests",
            "description",
            "check_in",
            "check_out",
        ]
