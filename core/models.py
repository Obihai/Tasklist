from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'
    
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null = True)
    completed = models.BooleanField(default=False)

    priority = models.IntegerField(choices=Priority.choices, default=Priority.HIGH)
    
    class Meta:
        ordering = ['completed', 'due_date']

    def __str__(self):
        return f'{self.title} ({self.get_priority_display()})'
    