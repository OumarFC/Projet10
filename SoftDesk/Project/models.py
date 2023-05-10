from django.db import models
from django.conf import settings


class Project(models.Model):
    PROJECT_TYPES = [
                    ('BE', 'Back-end'),
                    ('FE', 'Front-end'),
                    ('IOS', 'IOS'),
                    ('ANDROID', 'Android'),
                    ]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=PROJECT_TYPES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT,
                               related_name='project_created_by'
                               )

    def __str__(self):
        return self.title
