from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role')



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role')
        extra_kwargs = {'password': {'write_only' : True}}


        def create(self, validated_data):
            user = User.objects.create_user(validated_data['email'], validated_data['username'], validated_data['password'], validated_data['role'])

            return user