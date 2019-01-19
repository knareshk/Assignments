from django.db import models

# Create your models here.


class Name(models.Model):
    name_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name_id = models.ForeignKey(Name)
    phn_num = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url


class Address(models.Model):
    details = models.ForeignKey(Contact)
    addr = models.CharField(max_length=300)
    #date = models.DateField()

    def __str__(self):
        return self.addr
