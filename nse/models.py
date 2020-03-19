from django.db import models

# Create your models here.
class Equities(models.Model):
    symbol = models.CharField(max_length=100)
    series = models.CharField(max_length=30)
    open = models.DecimalField(max_digits=30, decimal_places=2)
    high = models.DecimalField(max_digits=30, decimal_places=2)
    low = models.DecimalField(max_digits=30, decimal_places=2)
    close = models.DecimalField(max_digits=30, decimal_places=2)
    last = models.DecimalField(max_digits=30, decimal_places=2)
    prevclose = models.DecimalField(max_digits=30, decimal_places=2)
    tottrdqty = models.IntegerField()
    timestamp = models.DateField()
    
    def __str__(self):
        return self.symbol