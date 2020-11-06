from django.db import models
from django.core.validators import MinValueValidator


class Fibonachi(models.Model):
    number_input = models.IntegerField(verbose_name="Исходное число")
    number_output = models.IntegerField(verbose_name="Результат")

    def __str__(self):
        return f"{self.number_input}"
