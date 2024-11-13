from django.db import models


from django.db import models

class UserImage(models.Model):
    username = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username
