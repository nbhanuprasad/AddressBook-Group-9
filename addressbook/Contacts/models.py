from django.db import models
from django.contrib.auth.models import User

class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.DateField(null=True)
    phnumber = models.IntegerField(max_length=15, null=True)
    phnumberalt= models.IntegerField(max_length=15, null=True, blank=True)
    Staddress= models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    zipcode = models.IntegerField(max_length=7, null=True)
    country = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.fname
# Create your models here.
