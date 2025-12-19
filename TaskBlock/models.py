from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = [
        ("make", "Зробити"), 
        ("inprogress", "В процесі"), 
        ("complete", "Виконано"), 
        ("declined", "Відкладено"),
    ]
    PRIORITY_CHOICES = [
        ("ndi", "Не відкладно важливе"), 
        ("tmi", "Найважливіше"), 
        ("mi", "Важливіше"), 
        ("i", "Важливе"), 
        ("ni", "Не важливе"),
    ]

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='make', verbose_name="Статус")
    priorites = models.CharField(max_length=5, choices=PRIORITY_CHOICES, default='i', verbose_name="Пріоритет")
    datetocm = models.DateTimeField(verbose_name="Дата закінчення")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="Творець")

    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"
        ordering = ['priorites', 'datetocm'] 

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='coments', verbose_name="Коментар")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coments', verbose_name="Творець")
    text = models.TextField()
    upltime = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['upltime'] 

    def __str__(self):
        return self.text