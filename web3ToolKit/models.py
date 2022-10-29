from datetime import date
from lib2to3.pgen2 import token
from django.db import models
from django.test import TransactionTestCase

# Represents the data in your database
# Create your models here.


class wallet(models.Model):
    # id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=36)
    token = models.CharField(max_length=16)
    transactionValue = models.DecimalField(max_digits=100, decimal_places=0)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.address
