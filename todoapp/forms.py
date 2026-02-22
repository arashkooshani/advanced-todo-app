from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed','category','priority','due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
            'due_date': 'تاریخ سررسید',
            'priority': 'اولویت',
            'category': 'دسته‌بندی',
            'completed': 'انجام شده؟',
        }