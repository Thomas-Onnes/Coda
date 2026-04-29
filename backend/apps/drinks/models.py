from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Drink(TimeStampModel):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50, null=True, blank=True, unique=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    tried = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} - {self.name}"