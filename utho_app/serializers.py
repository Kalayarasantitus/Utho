from rest_framework import serializers
from .models import *

# class UserImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserImage
#         fields = ['username', 'image']

from rest_framework import serializers
from .models import UserFile

class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['username', 'file', 'file_type']