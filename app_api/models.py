from datetime import datetime
from django.db import models
from django.utils.timezone import localtime, now

# Create your models here.


class Task(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        
        if self.completed:
            self.completed_date = localtime(now())
        else:
            self.completed_date = None

        super(Task, self).save(*args, **kwargs)