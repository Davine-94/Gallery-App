from .views import *
from django.urls import path

urlpatterns = [
    path('', gallery, name='gallery'),
    path('search/', search_images, name='search_images'),
    path('category/<category>', view_category, name='view_category'),
    path('location/<location>', view_location, name='view_location')
]
