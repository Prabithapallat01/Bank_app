from django.shortcuts import render
from rest_framework.utils.representation import serializer_repr

from .serializers import UserRegisterSerializer,LoginSerializer,BranchSerializer,WithdrawSerailizer,DepositeSerailizer
from .models import Branch
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login,logout,authenticate
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.




class AccountCreate(APIView):
    def get(self,request):
        account=Branch.objects.all()
        serializer=BranchSerializer(account,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BalanceApiView(APIView):
    def get(self,request,account_number):
        account_number=Branch.objects.get(account_number=account_number)
        serializer=BranchSerializer(account_number)
        return Response(serializer.data)


class Register(APIView):
    def get(self,request):
        account=User.objects.all()
        serializer=UserRegisterSerializer(account,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="registered"
            data['first_name']=account.first_name
            data['username']=account.username
            data['password']=account.password
            data['email']=account.email

        else:
            data=serializer.errors
        return Response(data)


class LoginUser(APIView):

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            # user = authenticate(request, username=username, password=password)
            user=User.objects.get(username=username)
            if (user.username==username)&(user.password==password):
                login(request, user)
                token,created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"loginfailed"})


class LogoutUser(APIView):
    def post(self,request):
        logout(request)
        request.user.auth_token.delete()



class WithdrawView(APIView):

    def post(self,request,account_number):
        serializer=WithdrawSerailizer(data=request.data)
        accno=Branch.objects.get(account_number=account_number)
        if serializer.is_valid():
            amount=serializer.validated_data.get("amount")
            if amount<accno.balance:
                accno.balance-=amount
                accno.save()
                return Response({"balance is debited now & Your Current Balance is ":accno.balance})
            else:
               return Response({"message":"insuffiecient Balance:"})


class DepositeApiView(APIView):
    def post(self,request,account_number):
        serializer=DepositeSerailizer(data=request.data)
        accno=Branch.objects.get(account_number=account_number)
        if serializer.is_valid():
            amount=serializer.validated_data.get("amount")
            accno.balance+=amount
            accno.save()
            return Response({"Your Account is Credited now and Your Current Balance is":accno.balance})


# class TransactionApi(APIView):
#     def post(self,request,acc_no):
#         serializer=TransactionTransfer(data=request.data)
#         accno=BankStatement.objects.get(acc_no=acc_no)
#         if serializer.is_valid():
#             amnt = serializer.validated_data.get("amnt")
#             receiver = serializer.validated_data.get("receiver")
#             receiver_accno=serializer.validated_data.get("receiver_accno")
#             if accno.balance<amnt:
#                 user = BankStatement.objects.get(receiver)
#                 if (user.receiver == receiver) & (user.receiver_accno == receiver_accno):
#                         accno.balance-=amnt
#                         return Response({"message": "balnce is transfered"})
#                 else:
#                     return Response({"message":"insuffiecient Balance:"})
#


