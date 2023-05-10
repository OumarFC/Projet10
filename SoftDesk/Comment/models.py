from django.db import models

from Issue.models import Issue
from django.conf import settings


class Comment(models.Model):
    description = models.CharField(max_length=128, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT,
                               related_name='user_comment'
                               )
    issue = models.ForeignKey(Issue,
                              on_delete=models.CASCADE,
                              related_name='issue_comment')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"
