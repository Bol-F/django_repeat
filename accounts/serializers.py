from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Account

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  )
        read_only_fields = ('id',)


class AccountRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=128)
    password_confirm = serializers.CharField(write_only=True, min_length=8, max_length=128)

    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'password',
                  'password_confirm',)
        read_only_fields = ('id',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match."}
                                          )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
