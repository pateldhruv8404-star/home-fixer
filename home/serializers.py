from rest_framework import serializers
from .models import User


#==========Logout Serializer ==========#
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


#==========Otp sent and verification serializers ==========#
class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

#===========Verify OTP Serializer ==========#
class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

#===========Complete Registration Serializer ==========#
class CompleteRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=20)

    role = serializers.ChoiceField(
        choices=['CUSTOMER', 'SERVICEMAN', 'VENDOR'],
        default='CUSTOMER'
    )

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "User with this email already exists"
            )
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits"
            )
        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits"
            )
        return value


#===========User Profile Serializer ==========#
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'role',
            'is_verified',
        ]
