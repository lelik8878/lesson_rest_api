
from django.urls import path
from api.views import get_products, save_data_to_db

urlpatterns = [
    path('products/', get_products),
    path('save_to_db/', save_data_to_db),
]