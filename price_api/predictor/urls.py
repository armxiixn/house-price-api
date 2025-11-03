from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_price, name='predict_price'),
    path('regions/', views.get_region_prices, name='get_region_prices'),
]
