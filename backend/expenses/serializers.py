from rest_framework import serializers
from api.serializers import UserPublicSerializer
from .models import Transaction,Category
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'user',
            'name',
            'description'
        ]

class TransactionSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True) 
    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'category',
            'category_name',
            'amount',
            'date',
            'description',
            'created_at',
            'updated_at'
        ]
    
    def validate_amount(self,value):
        if value < 0:
            raise serializers.ValidationError("Amount must be positive value")
        return value

class NestedTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields=[
            'id',
            'amount',
            'description',
            'date'
        ]

class MonthlyExpenseSummarySerializer(serializers.Serializer):
    category_id = serializers.CharField()
    category_name = serializers.CharField()
    date_year = serializers.CharField()
    # date__month = serializers.CharField()
    total_transaction = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    transactions = NestedTransactionSerializer(many=True) 