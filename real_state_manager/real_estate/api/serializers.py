from rest_framework import serializers

from real_state_manager.real_estate.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
