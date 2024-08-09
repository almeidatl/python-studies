from django.db import models

# Create your models here.
class Task(models.Model):
    """
    A model representing a task with a title, description, and completion status.

    Attributes:
    title (CharField): The title of the task. Maximum length is 100 characters.
    description (TextField): The detailed description of the task.
    completed (BooleanField): Indicates whether the task is completed or not. Defaults to False.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title