from django.db import models
from django.contrib.auth.models import User




class Plan(models.Model):
    """Reja uchun model"""

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Plan'


class Team(models.Model):
    """Jamoalar uchun model"""

    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name="crated_teams", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Team"