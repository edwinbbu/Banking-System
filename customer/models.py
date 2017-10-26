import uuid

from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    age=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    street=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50, default="India")
    pin_code=models.IntegerField(null=True)
    balance=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Balance")
    account_no=models.CharField(max_length=200,editable=False)

    def __str__(self):
        return str(self.user)

    def acc_no(self):
        acc_no="ACC"+str(self.pk)
        return acc_no

    def get_balance(self,amount ,code):
        amount = Decimal(amount)
        balance = Decimal(self.balance)
        if code == 1:
            if balance > amount:
                balance=balance-amount
                return balance
            else:
                return -1
        else:
            balance=balance+amount
            return balance
