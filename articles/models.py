from django.db import models
from datetime import datetime


class Article(models.Model):
    head = models.CharField(max_length=255)
    description = models.TextField(max_length=16384)
    image = models.CharField(max_length=255, default='')
    views = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def increment_views(self):
        self.views += 1
