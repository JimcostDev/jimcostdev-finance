from decimal import Decimal
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from finances.models import Income, Expense, Setting

class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Obtener los parámetros de fecha
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Se requieren start_date y end_date como parámetros."}, status=400)

        # Convertir a formato de fecha
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Formato de fecha inválido. Use YYYY-MM-DD."}, status=400)

        # Filtrar ingresos y gastos por rango de fechas
        incomes = Income.objects.filter(user=request.user, date__range=(start_date, end_date))
        expenses = Expense.objects.filter(user=request.user, date__range=(start_date, end_date))

        # Calcular ingresos brutos
        total_income = sum(income.amount for income in incomes)

        # Calcular gastos totales
        total_expenses = sum(expense.amount for expense in expenses)

        # Calcular diezmos y ofrendas
        tithe = total_income * Decimal('0.1')  # 10% de diezmos
        offering_percentage = Decimal(Setting.get_value("offering_percentage", default=4.00))  # Convertir a Decimal
        offering = total_income * (offering_percentage / Decimal('100'))

        # Aportes a la iglesia
        church_contribution = tithe + offering

        # Calcular ingresos netos
        net_income = total_income - church_contribution

        # Calcular balance final
        final_balance = net_income - total_expenses

        # Responder con el reporte
        return Response({
            "start_date": start_date,
            "end_date": end_date,
            "total_income": float(total_income),  # Convertir a float para JSON
            "total_expenses": float(total_expenses),
            "tithe": float(tithe),
            "offering": float(offering),
            "church_contribution": float(church_contribution),
            "net_income": float(net_income),
            "final_balance": float(final_balance)
        })
