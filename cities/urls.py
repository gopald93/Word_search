from django.urls import path
from .views import create,search
from .rest_view import search_api
urlpatterns = [
    path('create/', create, name='create'),
    path('search/', search, name='search'),
    path('search_api/', search_api, name='search_api'),
]