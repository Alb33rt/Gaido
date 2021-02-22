from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    details = models.TextField(max_length=1024, verbose_name=("Additional Information"), blank = True, null = True)
    photo = models.ImageField(verbose_name=('Photo'), upload_to='photos/', default='photos/default_avatar.png')
    
    def __str__(self):
        return f"{self.username}"