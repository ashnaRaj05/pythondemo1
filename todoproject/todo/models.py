from django.db import models


# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=244)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.name
