from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Entry(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100, default='')
    site_email_used = models.EmailField(max_length=100, blank=True, default='')
    site_password_used = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.author.username} Entry {self.pk}'


class MasterPassword(models.Model):
    author = models.OneToOneField(
        User, on_delete=models.CASCADE)
    master = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return f'{self.author.username} hashed Master Password'
