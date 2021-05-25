from rest_framework import serializers

from api.models import UUIDRequest


class UUIDSerializer(serializers.ModelSerializer):
    key_value = serializers.SerializerMethodField
    class Meta:
        model = UUIDRequest
        fields = ['key_value', 'uuid', ]

    def get_key_value(self):
        return self.key_value