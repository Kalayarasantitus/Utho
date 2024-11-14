from django.urls import path
from .views import UserFileUploadView, UserFileListView, UserFileDetailView

urlpatterns = [
    path('upload/', UserFileUploadView.as_view(), name='file-upload'),
    path('<str:username>/<str:file_type>/', UserFileListView.as_view(), name='file-list'),
    path('<int:file_id>/', UserFileDetailView.as_view(), name='file-detail'),
]