from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('search/', views.SearchResult, name='search'),  # Example URL pattern for search page
    path('search-results/', views.SearchResult, name='search_results'),
]