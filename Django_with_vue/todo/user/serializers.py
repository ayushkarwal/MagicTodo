from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    # def create(self, validated_data):
    #     import pdb;pdb.set_trace()
    #     return User.objects.create_user(**validated_data)