from django.urls import path
from .views import UserImageUploadView
from utho_app import urls

urlpatterns = [
    path('upload/', UserImageUploadView.as_view(), name='upload-image'),
]
