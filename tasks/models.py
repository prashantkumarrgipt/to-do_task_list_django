from django.db import models

# Create your models here.

class Task(models.Model):
    # Unique ID - Primary key
    id = models.AutoField(primary_key=True)

    # Title of the task
    title = models.CharField(max_length=255)

    # Boolean field to determine whether the task has been completed
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.title}"

