from django.db import models

# Create your models here.


class Phone(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Tab(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Watch(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Airpod(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class PhoneRate(models.Model):
    phone = models.ForeignKey(
        Phone, related_name='phonerate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class TabRate(models.Model):
    tab = models.ForeignKey(
        Tab, related_name='tabrate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class AirpodRate(models.Model):
    airpod = models.ForeignKey(
        Airpod, related_name='airpodrate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class WatchRate(models.Model):
    watch = models.ForeignKey(
        Watch, related_name='watchrate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class PhonesCover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')


class TabsCover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')


class WatchesCover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')


class AirpodsCover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')
