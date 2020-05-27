from django.db import models

# Create your models here.


class Task(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title