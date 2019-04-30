from django.urls import path
from crm_food.views import (
    TableCreateView, TableDetailView,
    RoleCreateView, RoleDetailView,
    DepartmentCreateView, DepartmentDetailView,
    StatusCreateView, StatusDetailView,
    ServicePercentageViewList, GetServicePersentageViewId,
    MealCategoryViewList, GetCategoryViewId,
    MealViewList, GetMealViewId, OrderViewList,
    GetOrderViewId, CheckViewList, GetCheckViewId,
    )
# from crm_food.views import index

urlpatterns = [
    path('tables/',TableCreateView.as_view(),name="tables"),
    path('tables/<int:pk>/',TableDetailView.as_view(), name='details'),
    path('roles/',RoleCreateView.as_view(), name="roles"),
    path('roles/<int:pk>/',RoleDetailView.as_view(), name="roles_detail"),
    path('departments/', DepartmentCreateView.as_view(), name="departments"),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name="departments_detail"),
    path('statuses/', StatusCreateView.as_view(), name="statuses"),
    path('statuses/<int:pk>/', StatusDetailView.as_view(), name="statuses_detail"),
    path('servicepercentages/', ServicePercentageViewList.as_view(), name="services"),
    path('servicepercentages/<int:pk>/', GetServicePersentageViewId.as_view(), name="services_detail"),
    path('mealcategories/', MealCategoryViewList.as_view(), name="categories"),
    path('mealcategories/<int:pk>/', GetCategoryViewId.as_view(), name="categories_detail"),
    path('meals/', MealViewList.as_view()),
    path('meals/<int:pk>/', GetMealViewId.as_view()),
    path('orders/', OrderViewList.as_view()),
    path('orders/<int:pk>/', GetOrderViewId.as_view()),
    path('checks/', CheckViewList.as_view()),
    path('checks/<int:pk>/', GetCheckViewId.as_view()),
    # path('',index,name='index')
]
