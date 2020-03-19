from django.db import models

# Create your models here.
class Equities(models.Model):
    symbol = models.CharField(max_length=100)
    series = models.CharField(max_length=30)
    open = models.DecimalField()
    high = models.DecimalField()
    low = models.DecimalField()
    close = models.DecimalField()
    last = models.DecimalField()
    prevclose = models.DecimalField()
    tottrdqty = models.IntegerField()
    timestamp = models.DateField()    

    class Meta:
      db_table = "equities"
    
    def __str__(self):
        return self.symbol