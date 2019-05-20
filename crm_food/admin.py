from django.contrib import admin
from crm_food.models import (
        Table, Role, MealCategory, Meal, Department,
        Check, Order, ServicePercentage, Status, CountMeals
    )

admin.site.register(Table)
admin.site.register(Role)
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Department)
admin.site.register(ServicePercentage)
admin.site.register(Order)
admin.site.register(Check)
admin.site.register(Status)
admin.site.register(CountMeals)





# Register your models here.
