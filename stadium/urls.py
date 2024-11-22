from django.urls import path
from .views import (get_category_of_service, get_type_of_services, get_type_of_sub_services,
                    get_specific_object, Category, save_or_create, PeopleListView)
urlpatterns = [
    path('', get_category_of_service),
    path('type_of_services/', get_type_of_services),
    path('type_of_sub_services/', get_type_of_sub_services),
    path('specific_object/', get_specific_object),
    path('create_category/', Category.as_view()),
    path('save_or_create/', save_or_create),
    path('people_category/', PeopleListView.as_view()),
]