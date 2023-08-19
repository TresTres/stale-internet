from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from subjects.models import Subject, Comment
from themes.models import Theme

class ReactionCategory(models.Model):
    name = models.CharField(max_length=200)
    content = models.JSONField()
    

class Reaction(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ReactionCategory, on_delete=models.SET_NULL, null=True)
    flavor_text = models.CharField(max_length=200) 
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    
    def clean(self):
        target_count = sum(field is not None for field in [self.comment, self.subject, self.theme])
        if target_count != 1:
            raise ValidationError('Reaction must be toward a single comment, subject, or theme.')