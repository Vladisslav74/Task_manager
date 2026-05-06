from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Приоритет задачи от 1(низкий) до 5(самый важный)"
    )
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title