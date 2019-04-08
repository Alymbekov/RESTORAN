from django.contrib import admin
from crm_food.models import (
        Table, Role, MealCategory, Meal, Department,
    )

admin.site.register(Table)
admin.site.register(Role)
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Department)




# Register your models here.
