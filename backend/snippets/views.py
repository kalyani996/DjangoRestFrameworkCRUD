from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, mixins, permissions, renderers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

class SnippetsListCreateAPIView(
    generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


    def perform_create(self, serializer):
            print(serializer.validated_data)
            # email = serializer.validated_data.pop('email')
            # print(email)
            title = serializer.validated_data.get('title')
            code = serializer.validated_data.get('code') or None
            if code is None:
                 code = title
            serializer.save(owner=self.request.user) #form.save() model.save()
            
snippet_list_create_view = SnippetsListCreateAPIView.as_view()


class SnippetsDetailAPIView(
    generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

snippet_detail_view = SnippetsDetailAPIView.as_view()

class SnippetsUpdateAPIView(
    generics.UpdateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    loopup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

snippet_update_view = SnippetsUpdateAPIView.as_view()

class SnippetsDestroyAPIView(
    generics.DestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    loopup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_destroy(self,instance):
       super().perform_destroy(instance)

snippet_destroy_view = SnippetsDestroyAPIView.as_view()


class UserList(generics.ListAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'snippet':reverse('snippet-list', request=request, format=format),
    })

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)