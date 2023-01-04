from django.db import models
from django.contrib.auth.models import User



class Team(models.Model):
    """Jamoalar uchun model"""
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name="crated_teams", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Team"
