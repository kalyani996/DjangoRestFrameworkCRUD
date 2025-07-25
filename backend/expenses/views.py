from django.shortcuts import render
from .models import Category,Transaction
from .serializers import CategorySerializer, TransactionSerializer, MonthlyExpenseSummarySerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user) | Category.objects.filter(user__isnull = True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False,methods=['get'])
    def popular(self, request):
        popular_categories = Category.objects.annotate(num_transactions=
                                                       Count('transactions')).filter(num_transactions__gt=1).order_by('-num_transactions')[:5]
        serializer = self.get_serializer(popular_categories,many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """
        Custom action to activate a specific category.
        Accessed via /api/expenses/categories/{id}/activate/
        'detail=True' means this action applies to a single instance endpoint (e.g., /categories/1/activate).
        'methods=['post']' specifies that it only responds to POST requests.
        """
        category = self.get_object() # get_object() works because detail=True
        print(request)
        category.name = request.data.get('name')
        category.save()
        serializer = self.get_serializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        When creating a new transaction, automatically assign the current user.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Ensures the user of the transaction being updated remains the current user.
        """
        serializer.save(user=self.request.user)

class MonthyExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            raise Response({'details':'Please provide year and month as query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
            month = int(month)
            if not (1 <= month <= 12):
                raise ValueError("Month must be equal to 1 to 12")
        except ValueError:
            return Response({'detail':'Invalid year or month format'}, status=status.HTTP_400_BAD_REQUEST)
        
        monthly_transaction = Transaction.objects.filter(
            user=user,
            date__year=year,
            date__month=month
            ).select_related('category')
       
        #prepare summary and transaction together
        grouped_data = {}
        for transaction in monthly_transaction:
            category_id = transaction.category.id if transaction.category else None
            category_name = transaction.category.name if transaction.category else 'uncategorized'
            if category_id not in grouped_data: 
                grouped_data[category_id] ={
                    'category_id': category_id,
                    'category_name':category_name,
                    'date_year': transaction.date,
                    'total_amount':0,
                    'total_transaction':0,
                    'transactions':[]
                }
            grouped_data[category_id]['total_amount'] += transaction.amount
            grouped_data[category_id]['total_transaction'] += 1
            grouped_data[category_id]['transactions'].append(transaction)
        
        # Convert the dictionary of grouped data into a list of values
        # The values are the dictionaries that MonthlyExpenseSummarySerializer expects
        summary_list = list(grouped_data.values())
        summary_serializer = MonthlyExpenseSummarySerializer(summary_list,many=True)
        #individual summmary and transaction passed to API
        # print(monthly_transaction   )
        # summary_data = monthly_transaction.values('category__name','date__year','date__month').annotate(total_amount=Sum('amount'),transaction_count=Count('id')).order_by('category__name')
        # print(summary_data)
        # summary_serializer = MonthlyExpenseSummarySerializer(summary_data,many=True)

        #  # 2. Prepare Individual Transactions Data
        # # Use TransactionSerializer for the individual transactions
        # transactions_serializer = TransactionSerializer(monthly_transaction, many=True)
        
        # # Combine both into a single response
        # response_data = {
        #     "summary": summary_serializer.data,
        #     "transactions": transactions_serializer.data
        # }

        return Response(summary_serializer.data)
        