from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Branch



class BranchSerializer(ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','email','username','password']
    def reguser(self):
        rgstr=User(
            first_name=self.validated_data['first_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password']
        )
        rgstr.save()


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class WithdrawSerailizer(serializers.Serializer):

    amount=serializers.IntegerField()

class DepositeSerailizer(serializers.Serializer):

    amount=serializers.IntegerField()


# class TransactionTransfer(ModelSerializer):
#
#     class Meta:
#         model=BankStatement
#         fields='__all__'
