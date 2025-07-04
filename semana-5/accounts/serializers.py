from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfileSerializaer"""
    class Meta:
        """Meta model"""
        model = UserProfile
        fields = ['bio', 'phone', 'avatar', 'birth_date']


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer"""
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        """Meta model"""
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'profile']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("El password no coincide")
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya esta siendo usando")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya esta en uso")
        return value

    def create(self, validated_data):
        validated_data.pop('password_confirm', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user
    

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        # Update del usuario
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update del perfil
        if profile_data:
            profile = instance.profile
            for attr, value, in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return instance
