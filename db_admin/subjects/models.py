from django.db import models
from django.contrib.auth.models import User

from themes.models import Theme


class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"subject-{self.pk}-{self.title[:15]}"

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    original_subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children_comments')
    previous_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_comment')
    text_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.comment[:60] + "..."
