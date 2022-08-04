from dataclasses import field
from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=225)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone_number']

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='user already exist')

        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(
                detail='user with email already exist')

        phone_number_exists = User.objects.filter(
            phone_number=attrs['phone_number']).exists()
        if phone_number_exists:
            raise serializers.ValidationError(
                detail='user with phone number already exist')
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']


        )

        user.set_password(validated_data['password'])
        user.save()
        return user
