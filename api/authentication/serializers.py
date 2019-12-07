from rest_framework import serializers
from authentication.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('dob','adhaar', 'phone', 'accountNumber', 'accountIFSC', 'accountBranch', 'photo')


class UserSignUpSerializer(serializers.ModelSerializer):
    UserProfile = UserProfileSerializer(required=True, many=False)

    class Meta:
        model = User
        fields = ('email','username', 'first_name', 'last_name','password', 'UserProfile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if (User.objects.filter(username=validated_data.get('email')).exists()):
            return {'status': 'failed', 'message': 'Email already registered'}

        profile_data = validated_data.pop('UserProfile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('UserProfile')
        UserProfile = instance.UserProfile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        UserProfile.phone = profile_data.get('phone', UserProfile.phone)
        UserProfile.dob = profile_data.get('dob', UserProfile.dob)
        UserProfile.adhaar = profile_data.get('adhaar', UserProfile.adhaar)
        UserProfile.accountNumber = profile_data.get('accountNumber', UserProfile.accountNumber)
        UserProfile.accountIFSC = profile_data.get('accountIFSC', UserProfile.accountIFSC)
        UserProfile.accountBranch = profile_data.get('accountBranch', UserProfile.accountBranch)
        UserProfile.photo = profile_data.get('photo', UserProfile.photo)
        UserProfile.save()

        return instance

class UserUpdateSerializer(serializers.ModelSerializer):
    UserProfile = UserProfileSerializer(required=True, many=False)

    class Meta:
        model = User
        fields = ('pk', 'email','username', 'first_name', 'last_name', 'UserProfile')
        # extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('UserProfile')
        UserProfile = instance.UserProfile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        UserProfile.phone = profile_data.get('phone', UserProfile.phone)
        UserProfile.dob = profile_data.get('dob', UserProfile.dob)
        UserProfile.adhaar = profile_data.get('adhaar', UserProfile.adhaar)
        UserProfile.accountNumber = profile_data.get('accountNumber', UserProfile.accountNumber)
        UserProfile.accountIFSC = profile_data.get('accountIFSC', UserProfile.accountIFSC)
        UserProfile.accountBranch = profile_data.get('accountBranch', UserProfile.accountBranch)
        UserProfile.photo = profile_data.get('photo', UserProfile.photo)
        UserProfile.save()

        return instance