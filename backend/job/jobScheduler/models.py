from django.db import models

# Create your models here.
class Job(models.Model):
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    status_choices = [
        ('pending', 'Pending'), 
        ('running', 'Running'), 
        ('failed', 'Failed')
    ]
    taskName = models.CharField(max_length=255)
    payload = models.JSONField()
    priority = models.CharField(max_length=10, choices=priority_choices)
    status = models.CharField(max_length=10, choices=status_choices, default="pending")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskName