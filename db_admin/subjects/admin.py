from django.contrib import admin

from subjects.models import Subject, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'author', 'timestamp')
    
    inlines = [
        CommentInline,
    ]
