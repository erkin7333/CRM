from django.db import models
from django.contrib.auth.models import User


"""Foydalanuvchi Profili uchun Model"""
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Userprofile"
