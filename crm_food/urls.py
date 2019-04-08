from django.urls import path
from crm_food.views import index

urlpatterns = [
    path('',index,name='index')
]
