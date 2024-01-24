from django.urls import path
from recipes.views import my_view, sobre

urlpatterns = [
    path('', my_view),  # home
    path('sobre/', sobre)
]
