from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
# Create your models here.

class USerProfileManager(BaseUserManager):
    # este es el manager 
    def create_user(self,email,name,phone,password=None,**extra_fields):
        if not email and phone:
            raise ValueError('Necesita introducir email y telefono')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name,phone = phone)
        
        user.password = make_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email,name, phone,password,**extra_fields):
        user = self.create_user(email,name,phone,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)
        return user



        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length= 50)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default= False)
    objects = USerProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']


    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email