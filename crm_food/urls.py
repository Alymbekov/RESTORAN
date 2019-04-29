from django.urls import path
from crm_food.views import (
    TableViewList, GetTableViewId,
    RoleViewList, GetRoleViewId,
    DepartmentViewList, GetDepartmentViewId,
    GetStatusViewId, StatusViewList,
    ServicePercentageViewList, GetServicePersentageViewId,
    MealCategoryViewList, GetCategoryViewId,
    MealViewList, GetMealViewId, OrderViewList,
    GetOrderViewId, CheckViewList, GetCheckViewId,
    )
from crm_food.views import index

urlpatterns = [
    path('tables/',TableViewList.as_view(),name="tables"),
    path('tables/<int:pk>/',GetTableViewId.as_view()),
    path('tables/1/', GetTableViewId.as_view()),
    path('roles/',RoleViewList.as_view()),
    path('roles/<int:pk>/',GetRoleViewId.as_view()),
    path('departments/', DepartmentViewList.as_view()),
    path('departments/<int:pk>/', GetDepartmentViewId.as_view()),
    path('statuses/', StatusViewList.as_view()),
    path('statuses/<int:pk>/', GetStatusViewId.as_view()),
    path('servicepercentages/', ServicePercentageViewList.as_view()),
    path('servicepercentages/<int:pk>/', GetServicePersentageViewId.as_view()),
    path('mealcategories/', MealCategoryViewList.as_view()),
    path('mealcategories/<int:pk>/', GetCategoryViewId.as_view()),
    path('meals/', MealViewList.as_view()),
    path('meals/<int:pk>/', GetMealViewId.as_view()),
    path('orders/', OrderViewList.as_view()),
    path('orders/<int:pk>/', GetOrderViewId.as_view()),
    path('checks/', CheckViewList.as_view()),
    path('checks/<int:pk>/', GetCheckViewId.as_view()),
    path('',index,name='index')
]
