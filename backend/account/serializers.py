from rest_framework import serializers
from django.contrib.auth.models import User

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','last_login']
        read_only_fields = ['first_name', 'last_name', 'username','last_login']

class PrivateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['last_login']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user