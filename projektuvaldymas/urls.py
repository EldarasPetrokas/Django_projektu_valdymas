from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projektai/', views.projektai_list, name='projektai_list'),
    path('projektai/<uuid:pk>/', views.projektas_detail, name='projektas_detail'),
    path('register/', views.register, name='register'),
]

