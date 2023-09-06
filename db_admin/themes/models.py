from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Theme(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"theme-{self.pk}-{self.title[:15]}"