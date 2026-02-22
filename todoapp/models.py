from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Task(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    due_date=models.DateField(null=True, blank=True)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    priority=models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    def __str__(self):
        return self.title

class Category(models.Model):
    TYPE_CHOICES = [
        ('WORK', 'Work'),
        ('PERSONAL', 'Personal'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='WORK'
    )
    def __str__(self):
        return self.name




