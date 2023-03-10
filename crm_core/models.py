from django.db import models
from django.contrib.auth.models import User
from team.models import Team


class Lead(models.Model):
    LOW = 'PAST'
    MEDIUM = "O'rta"
    HIGH = 'YUQORI'
    CHOICES_PRIORITY = (
        (LOW, 'PAST'),
        (MEDIUM, "O'rta"),
        (HIGH, "YUQORI")
    )
    NEW = "YANGI"
    CONTACTED = "ALOQA QILGAN"
    WON = "YUTUQ"
    LOST = "YO'QOTILGAN"

    CHOICES_STATUS = (
        (NEW, "YANGI"),
        (CONTACTED, "ALOQA QILGAN"),
        (WON, 'YUTUQ'),
        (LOST, "YO'QOTILGAN")
    )

    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, default=NEW)
    converted_to_client = models.BooleanField(default=False, verbose_name="Mijozga aylantirildi")
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Lead'
        ordering = ('name',)



class LeadFile(models.Model):
    team = models.ForeignKey(Team, related_name="lead_files", on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='files', on_delete=models.CASCADE)
    files = models.FileField(upload_to='leadfiles/')
    created_by = models.ForeignKey(User, related_name='lead_files', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.created_by.username

    class Meta:
        verbose_name = "LeadFile"


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name="lead_comments", on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='lead_comments', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    def __str__(self):
        return self.created_by.username
    class Meta:
        verbose_name = "Comment"



