from django.urls import path

from . import views

urlpatterns = [
    path('',views.cowntdown_list_create_view,name='countdown-list'),
    path('<int:pk>/',views.cowntdown_detail_view,name='countdown-detail')
    # path('<int:pk>/update/',views.product_update_view, name='product-update'),
    # path('<int:pk>/delete/',views.product_destroy_view, name='product-destroy')
]