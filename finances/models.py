from django.db import models

class IncomeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='incomes')
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()  # Fecha en la que se recibió el ingreso
    
    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"

class Expense(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()  # Fecha en la que se realizó el gasto
    
    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"

class Setting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 4.00 para 4%
    
    def __str__(self):
        return f"{self.key}: {self.value}"
    
    @staticmethod
    def get_value(key, default=None):
        try:
            return Setting.objects.get(key=key).value
        except Setting.DoesNotExist:
            return default

class Report(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reports')
    month = models.DateField()  # Primer día del mes para identificar el reporte
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    net_income = models.DecimalField(max_digits=10, decimal_places=2)
    tithe = models.DecimalField(max_digits=10, decimal_places=2)
    offering = models.DecimalField(max_digits=10, decimal_places=2)
    church_contribution = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_offerings(self, total_income):
        # Obtener el porcentaje dinámico desde el modelo Setting
        offering_percentage = Setting.get_value("offering_percentage", default=4.00)
        return total_income * (offering_percentage / 100)

    def save(self, *args, **kwargs):
        # Calcular valores antes de guardar
        self.tithe = self.total_income * 0.1  # 10% para diezmos
        self.offering = self.calculate_offerings(self.total_income)
        self.church_contribution = self.tithe + self.offering
        self.net_income = self.total_income - self.church_contribution - self.total_expenses
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reporte de {self.user} - {self.month.strftime('%B %Y')}"
