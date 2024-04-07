from rest_framework import serializers
from .models import CustomUser

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True) 

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'referral_code', 'timestamp')


class UserRegisterSerializer(serializers.ModelSerializer):
    referral_code = serializers.CharField(max_length=10, required=False)
    points = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'referral_code', 'points')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        referral_code = validated_data.pop('referral_code', None)
        user = CustomUser.objects.create_user(**validated_data)
        
        if referral_code:
            user.referral_code = referral_code  # Assign referral code to user
            user.save()

            referred_by = CustomUser.objects.filter(referral_code=referral_code).first()
            if referred_by:
                referred_by.points += 1
                referred_by.save()

        return user


