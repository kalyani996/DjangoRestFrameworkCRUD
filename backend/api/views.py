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
                         