from django.db import models
from apps.account.models import Account
from apps.reason.models import Reason

class Transaction(models.Model):
  emitter = models.ForeignKey(Account, related_name='transactions_sent', on_delete=models.CASCADE)
  receiver = models.ForeignKey(Account, related_name='transactions_received', on_delete=models.CASCADE)
  amount = models.FloatField(default=0.00)
  date = models.DateTimeField(auto_now_add=True)
  reason = models.ForeignKey(Reason,on_delete=models.CASCADE)