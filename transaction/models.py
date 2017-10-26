from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.

class Transaction(models.Model):
    W="Withdrawal"
    D="Deposit"
    T="Account Transfer"
    CHOICES=(
        (W,"Withdrawal"),
        (D,"Deposit"),
        (T,"Account Transfer"),
    )
    previous_balance=models.DecimalField(max_digits=20,decimal_places=2)
    current_balance=models.DecimalField(max_digits=20,decimal_places=2)
    transaction_time=models.DateTimeField(default=datetime.datetime.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    transaction_id=models.CharField(max_length=100)
    type=models.CharField(max_length=50,choices=CHOICES)

    def __str__(self):
        return self.transaction_id

    def get_transaction_id(self):
        trans=str(self.user.username)+'_'+str(self.pk)
        return trans