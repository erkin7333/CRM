from django.db import models
from django.contrib.auth.models import User



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

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Lead'