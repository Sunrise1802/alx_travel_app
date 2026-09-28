from django.db import models


class Listing(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField()
     location = models.CharField(max_length=200)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     bedrooms = models.PositiveIntegerField()
     bathrooms = models.PositiveIntegerField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.title


# Create your models here.
