from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gen/<str:select>/', gen, name='gen'),
    path('ready_var/<int:pk>/<str:select>/', ready_var, name='ready_var'),
    path('task<int:num>/', get_task, name='get_task'),
]
