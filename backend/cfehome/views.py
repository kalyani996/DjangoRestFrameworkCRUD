from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response  import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from django.urls import reverse # Import reverse to dynamically get URLs




@api_view(['GET','POST'])
def api_home(request,*args,**kwargs):
    """
    DRF API View
    """
    if request.method == 'GET':
        # For GET request, return a welcome message and links to key API endpoints.
        # We try to reverse common URL names; if they don't exist, provide a generic path.
        
        endpoints = {}
        request_format = kwargs.get('format', None) # Get format from kwargs for reverse

        # --- Links for product-related URLs ---
        # Products app is included under 'api/products/' and namespaced as 'products'
        try:
            # Reversing 'products:product-list' will correctly build '/api/products/'
            products_list_create_path = reverse('product-list')
            endpoints['products_list_create'] = request.build_absolute_uri(products_list_create_path)
        except Exception as e:
            print(f"Error reversing 'products:product-list': {e}")
            endpoints['products_list_create'] = "/api/products/" # Fallback if reverse fails
        try:
        # Reversing 'category-list' for the CategoryViewSet list endpoint
            category_list_path = reverse('category-list')
            endpoints['expenses_categories_list_create'] = request.build_absolute_uri(category_list_path)
        except Exception as e:
            print(f"Error reversing 'category-list': {e}")
            endpoints['expenses_categories_list_create'] = "/api/expenses/categories/" # Fallback

        try:
            # Reversing 'transaction-list' for the TransactionViewSet list endpoint
            transaction_list_path = reverse('transaction-list')
            endpoints['expenses_transactions_list_create'] = request.build_absolute_uri(transaction_list_path)
        except Exception as e:
            print(f"Error reversing 'transaction-list': {e}")
            endpoints['expenses_transactions_list_create'] = "/api/expenses/transactions/" # Fallback

        try:
            # Reversing 'monthly-expense-summary' for the custom APIView
            summary_path = reverse('monthly_expenses_summary')
            endpoints['expenses_monthly_summary'] = request.build_absolute_uri(summary_path)
        except Exception as e:
            print(f"Error reversing 'monthly-expense-summary': {e}")
            endpoints['expenses_monthly_summary'] = "/api/expenses/summary/" # Fallback

        endpoints['expenses_base_url'] = request.build_absolute_uri("/api/expenses/")


        try:
            endpoints['admin_panel'] = request.build_absolute_uri(reverse('admin:index'))
        except Exception as e:
            print(f"Error reversing 'admin:index': {e}")
            endpoints['admin_panel'] = "/admin/"

        return Response({
            'message': 'Welcome to the Django REST Framework API Home Page!',
            'available_endpoints': endpoints,
            'instructions': 'Send a POST request to this endpoint with Product data to create a new product.'
        })


    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #serializer.save()
       # print(serializer.data)
       # data = serializer.data 
        return Response(serializer.data)

# @api_view(['GET'])
# def api_home(request,*args,**kwargs):
#     """
#     DRF API View
#     """
#     # if request.method != "POST":
#     #     return Response({"detail":"GET not allowed"},status=405)
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#        # data = model_to_dict(model_data,fields=['id','title','price'])
#     return Response(data)


















# def api_home(request,*args,**kwargs):
    # request -> HttpRequest -> Django
    # print(request.GET) #url query params
    # body = request.body
    # print(body) #byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) #string of JSON data -> Python Dict
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    #  model_data = Product.objects.all().order_by("?").first()
    #  data = {}
    #  if model_data:
         
          #model instance (model_data)
          #turn to python dict
        #   data = model_to_dict(model_data,fields=['id','title','price'])
         # json_data_str = json.dumps(data)
     #return HttpResponse(json_data_str,headers={"content-type":"application/json"})
          #return JSON to my client
    #  return JsonResponse(data)
                         