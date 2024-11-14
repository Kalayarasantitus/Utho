from django.db import models


# from django.db import models

# class UserImage(models.Model):
#     username = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.username


class UserFile(models.Model):
    username = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=50)  # Values: 'image', 'document', 'video'

    def __str__(self):
        return f"{self.username} - {self.file_type}"