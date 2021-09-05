from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for Account Model.
    """

    class Meta:
        model = Account
        fields = [
            'password',
            'email',
            'username',
        ]
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user