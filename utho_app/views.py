from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import UserFileSerializer
from .utils import upload_file_to_utho

class UserFileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserFileSerializer(data=request.data)
        if serializer.is_valid():
            user_file = serializer.save()
            response = upload_file_to_utho(user_file.file, user_file.file_type)
            if response:
                return Response({'message': 'File uploaded successfully', 'data': response,'file_id':user_file.id}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to upload to Utho'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserFileListView(APIView):
    def get(self, request, username, file_type, *args, **kwargs):
        files = UserFile.objects.filter(username=username, file_type=file_type)
        serializer = UserFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserFileDetailView(APIView):
    def delete(self, request, file_id, *args, **kwargs):
        try:
            user_file = UserFile.objects.get(id=file_id)
            user_file.delete()
            return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except UserFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)



    

    






#class UserImageUploadView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserImageSerializer(data=request.data)
#         if serializer.is_valid():
#             user_image = serializer.save()

#             # Pass the image file directly to `upload_image_to_utho`
#             response = upload_image_to_utho(user_image.image.file)
#             if response:
#                 return Response({'message': 'Image uploaded successfully', 'data': response}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'Failed to upload to Utho'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    