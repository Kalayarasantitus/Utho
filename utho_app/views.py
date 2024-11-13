from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserImage
from .serializers import UserImageSerializer
from .utils import upload_image_to_utho

class UserImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserImageSerializer(data=request.data)
        if serializer.is_valid():
            user_image = serializer.save()

            # Pass the image file directly to `upload_image_to_utho`
            response = upload_image_to_utho(user_image.image.file)
            if response:
                return Response({'message': 'Image uploaded successfully', 'data': response}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to upload to Utho'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
