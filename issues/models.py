from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Issue(models.Model):
    issue_title = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250)
    assigned_to = models.CharField(max_length=500)
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.issue_title + ' - ' + self.created_by