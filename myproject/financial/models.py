from django.db import models

class FinancialMovement(models.Model):
    TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.amount}"