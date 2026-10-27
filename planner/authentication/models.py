from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoises(models.TextChoices):

    DEVELOPER = 'Developer','Developer'

    ADMIN = 'Admin','Admin'

    PROJECT_COORDINATOR = 'Prooject Coordinator','Prooject Coordinator'

class Profile(AbstractUser):

    role = models.CharField(max_length=20,choices=RoleChoises.choices)

    class Meta :

        verbose_name = 'profiles'

        verbose_name_plural = 'profiles'

    def __str__(self):

        return self.username

    
