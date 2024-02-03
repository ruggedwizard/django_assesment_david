from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    EXPENSES_TYPES = (
        ('TRANSPORT','TRANSPORT'),
        ('FOOD','FOOD'),
        ('DATA','DATA'),
        ('MISCELLANEOUS','MISCELLANEOUS')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    amount = models.FloatField(null=False,blank=False)
    category = models.CharField(max_length=255, null=False, blank=False,choices=EXPENSES_TYPES, default='MISCELLANEOUS',error_messages={
        'invalid_choice':'Invalid value. Choose from {EXPENSES_TYPES}'
    })
    description = models.TextField(max_length=1024,null=False, blank=False)
    date=models.DateTimeField(auto_now_add=True)


class Budget(models.Model):
    BUDGET_TYPES = (
        ('TRANSPORT','TRANSPORT'),
        ('FOOD','FOOD'),
        ('DATA','DATA'),
        ('SAVINGS','SAVINGS'),
        ('MISCELLANEOUS','MISCELLANEOUS')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_budget')
    amount = models.FloatField(null=False,blank=False)
    category = models.CharField(max_length=255, null=False, blank=False,choices=BUDGET_TYPES, default='MISCELLANEOUS',error_messages={
        'invalid_choice':'Invalid value. Choose from {BUDGET_TYPES}'
    })