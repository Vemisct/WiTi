from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    datetocm = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label="Дата та час виконання 📅"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priorites', 'datetocm']
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Короткий заголовок завдання', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Детальний опис...', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priorites': forms.Select(attrs={'class': 'form-select'}),
        }
        
        labels = {
            'title': 'Заголовок ✏️',
            'description': 'Опис 📝',
            'status': 'Статус 🚦',
            'priorites': 'Пріоритет 🔥',
        }