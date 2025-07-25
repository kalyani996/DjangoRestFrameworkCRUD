from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TransactionViewSet, MonthyExpenseSummaryView

router = DefaultRouter()
router.register(r'categories',CategoryViewSet,basename='category')
router.register(r'transactions',TransactionViewSet,basename='transaction')

urlpatterns = [
    path('',include(router.urls)),
    path('summary',MonthyExpenseSummaryView.as_view(),name='monthly_expenses_summary'),
]