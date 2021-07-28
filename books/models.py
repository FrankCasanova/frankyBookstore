from django.db import models
from django.urls import reverse
from uuid import uuid4

# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default= uuid4,
        editable=False
    )
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
       return reverse('book_detail', args=[str(self.id)])
    