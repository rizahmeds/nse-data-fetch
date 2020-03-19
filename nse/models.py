from django.db import models

# Create your models here.
class Equities(models.Model):
    SYMBOL = models.CharField(max_length=100)
    SERIES = models.CharField(max_length=30)
    OPEN = models.DecimalField(max_digits=30, decimal_places=2)
    HIGH = models.DecimalField(max_digits=30, decimal_places=2)
    LOW = models.DecimalField(max_digits=30, decimal_places=2)
    CLOSE = models.DecimalField(max_digits=30, decimal_places=2)
    LAST = models.DecimalField(max_digits=30, decimal_places=2)
    PREVCLOSE = models.DecimalField(max_digits=30, decimal_places=2)
    TOTTRDQTY = models.IntegerField()
    TIMESTAMP = models.DateField()
    
    def __str__(self):
        return self.SYMBOL