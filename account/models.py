from django.db import models

# Create your models here.


class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/', null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
