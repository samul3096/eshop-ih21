from django.urls import path
from . import views

urlpatterns = [
    # '' this sign bcz after store there is nothing in url
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
]
