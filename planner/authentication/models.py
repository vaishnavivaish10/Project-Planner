from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoises(models.TextChoices):

    DEVELOPER = 'Developer','Developer'

    ADMIN = 'Admin','Admin'

    PROJECT_COORDINATOR = 'Prooject Coordinator','Prooject Coordinator'

class TechChoises(models.TextChoices):

    FRONtEND = 'Frontend Developer','Frontend Developer'
    BACKEND = 'Backend Developer','Backend Developer'
    FULLSTACK = 'Fullstack Developer','Fullstack Developer'
    UIUX = 'UI/UX Designer','UI/UX Designer'
    TESTER = 'Software Tester','Software Tester'

class Profile(AbstractUser):

    role = models.CharField(max_length=20,choices=RoleChoises.choices)

    tech = models.CharField(max_length=20,choices=TechChoises.choices,null=True,blank=True)

    class Meta :

        verbose_name = 'profiles'

        verbose_name_plural = 'profiles'

    def __str__(self):

        return f'{self.username}-{self.role}-{self.tech}'

    
