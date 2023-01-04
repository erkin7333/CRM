from django.db import models
from django.contrib.auth.models import User
from team.models import Team


class Client(models.Model):
    """Client uchun yaratilgan model"""

    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Client'
        ordering = ('name',)
