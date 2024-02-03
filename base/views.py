from django.shortcuts import render
from base.serializers import ExpenseSerializers, BudgetSerializers, RegisterSerializer
from base.models import Expense,Budget
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
def index_view(request):
    print("From the view")
    return Response({'message':'Assesment Submission'})

""" CREATE ACCOUNT VIEW"""
@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

""" EXPENSES VIEWS"""
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def expenses_view(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializers(expenses, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = ExpenseSerializers(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def expenses_detail(request,pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ExpenseSerializers(expense)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = ExpenseSerializers(expense,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""BUDGET VIEWS"""
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def budget_view(request):
    if request.method == 'GET':
        budgets = Budget.objects.all()
        serializer = BudgetSerializers(budgets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data 
        serializer = BudgetSerializers(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def budget_details(request,pk):
    try:
        budget=Budget.objects.get(pk=pk)
    except Budget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BudgetSerializers(budget)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BudgetSerializers(budget,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
