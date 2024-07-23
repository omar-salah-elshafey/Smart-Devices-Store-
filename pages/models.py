from django.db import models

# Create your models here.


class Logo(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Cover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class BlogCover(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')


class About(models.Model):
    cover = models.ImageField(upload_to='static/img/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Contact(models.Model):
    cover = models.ImageField(upload_to='static/img/')
    title = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    phone3 = models.CharField(max_length=14)
    mail = models.CharField(max_length=255)
    phonephoto = models.ImageField(upload_to='static/img/')
    mailphoto = models.ImageField(upload_to='static/img/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
