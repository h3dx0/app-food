import binascii
import os

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class User(AbstractUser):
    objects = UserManager()
    telephone = models.CharField(max_length=16, blank=True, null=True)
    business = models.ForeignKey('business.Business', on_delete=models.PROTECT, null=True, blank=True)
    type = models.ForeignKey('general_admin.UserType', on_delete=models.PROTECT, related_name='users', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios"
        ordering = ['first_name']


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, related_name='auth_token', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class UserType(models.Model):

    class Meta:
        verbose_name_plural = "Tipos Usuarios"
        ordering = ['type']

    USERS_TYPES = (
        ('USER', 'operator'),
        ('SUPERVISOR', 'supervisor'),
        ('CLIENT', 'client'),
        ('ADMIN', 'administrator'),
    )
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
