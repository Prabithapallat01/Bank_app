from django.db import models

# Create your models here
class Branch(models.Model):
    branch_name=models.CharField(max_length=250)
    account_number=models.IntegerField(default=True)
    bank_name=models.CharField(max_length=250)
    customer_name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    balance=models.IntegerField(default=0)

    def __str__(self):
        return self.branch_name


# class BankStatement(models.Model):
#
#     acc_no=models.ForeignKey(Branch,on_delete=models.CASCADE)
#     receiver_accno=models.CharField(max_length=10,default=True)
#     receiver=models.CharField(max_length=120)
#     amnt=models.IntegerField(default=0)


