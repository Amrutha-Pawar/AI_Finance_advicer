from django.urls import path
from . import views

urlpatterns = [
    path('advice/', views.finance_advice, name='finance_advice'),
]
