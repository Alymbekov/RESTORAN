from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from crm_food.models import (
    Table, Role, Department, Status,
    ServicePercentage, MealCategory,
    Meal, Order, Check
    )
from crm_food.serializers import (
    TableSerializer, RoleSerializer, DepartmentSerializer,
    StatusSerializer, ServicePercentageSerializer, MealCategorySerializer,
    MealSerializer, OrderSerializer, CheckSerializer,
    )

class CheckViewList(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class GetCheckViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class OrderViewList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class GetOrderViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MealViewList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class GetMealViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealCategoryViewList(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class GetCategoryViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class ServicePercentageViewList(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class GetServicePersentageViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class StatusViewList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class GetStatusViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DepartmentViewList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GetDepartmentViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class RoleViewList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class GetRoleViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TableViewList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class GetTableViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


def index(request):
    return HttpResponse("Hello world")
# Create your views here.
