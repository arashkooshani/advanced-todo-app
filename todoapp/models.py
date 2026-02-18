from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    due_date=models.DateField()
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


