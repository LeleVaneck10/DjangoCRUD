from django.urls import path
from . import views

urlpatterns = [
    
    path('product-list/', views.ShowAll, name='product-list/'),
    path('product-detail/<int:pk>', views.ViewProduct, name='product-list/'),
     
]
