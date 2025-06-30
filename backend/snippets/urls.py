from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   # path('',views.snippet_alt_view),
    #path('<int:pk>/',views.snippet_alt_view)
    path('',views.snippet_list_create_view,name='snippet-list'),
    path('<int:pk>/',views.snippet_detail_view,name='snippet-detail'),
    path('<int:pk>/update/',views.snippet_update_view, name='snippet-update'),
    path('<int:pk>/delete/',views.snippet_destroy_view, name='snippet-destroy'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('<int:pk>/highlight/', views.SnippetHighlight.as_view(),  name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)