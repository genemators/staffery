from django.urls import path
from . import views


urlpatterns = [
    path('tree/', views.home, name="home"),
    path('list/', views.list, name="list"),
]
