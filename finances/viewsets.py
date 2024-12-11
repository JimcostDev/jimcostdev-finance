from rest_framework import viewsets
from .serializers import IncomeCategorySerializer, ExpenseCategorySerializer, IncomeSerializer, ExpenseSerializer, ReportSerializer
from .models import IncomeCategory, ExpenseCategory, Income, Expense, Report
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

# Operaciones CRUD para IncomeCategory
@extend_schema(tags=['Income Categories'])
class IncomeCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()
    permission_classes = [IsAuthenticated]

# Operaciones CRUD para ExpenseCategory
@extend_schema(tags=['Expense Categories'])
class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseCategorySerializer
    queryset = ExpenseCategory.objects.all()
    permission_classes = [IsAuthenticated]

# Operaciones CRUD para Income
@extend_schema(tags=['Incomes'])
class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [IsAuthenticated]

# Operaciones CRUD para Expense
@extend_schema(tags=['Expenses'])
class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]


