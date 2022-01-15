from rest_framework import serializers
from myhue_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes user profiles"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class tblLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tblLocation
        fields = ('id', 'user_id', 'name')
        extra_kwargs = {'user_id': {'read_only': True}}
