from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from finances.viewsets import (
    IncomeCategoryViewSet,
    ExpenseCategoryViewSet,
    IncomeViewSet,
    ExpenseViewSet,
)

from finances.views import ReportView  # Vista personalizada para el reporte


# Crear un router único
router = DefaultRouter()
router.register('income-categories', IncomeCategoryViewSet, basename='income-category')
router.register('expense-categories', ExpenseCategoryViewSet, basename='expense-category')
router.register('incomes', IncomeViewSet, basename='income')
router.register('expenses', ExpenseViewSet, basename='expense')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/reports/', ReportView.as_view(), name='report-view'), 
    path('', include('docs.urls')),  # Documentación
]