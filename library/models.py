from datetime import datetime, timedelta

from django.db import models


# Create your models here.


class Person(models.Model):
    pid = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name) + ' ' + str(self.pid)


class Books(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.isbn)


def get_expire():
    date = datetime.today() + timedelta(days=15)
    return date.date()


class Issued(models.Model):
    pid = models.ForeignKey(Person, to_field='pid', on_delete=models.CASCADE, related_name='fpid')
    isbn = models.ForeignKey(Books, to_field='isbn', on_delete=models.CASCADE, related_name='fisbn')
    date_issued = models.DateField(auto_now_add=True)
    expires_on = models.DateField(default=get_expire)

    def __str__(self):
        return str(self.pid) + ' ' + str(self.isbn)
