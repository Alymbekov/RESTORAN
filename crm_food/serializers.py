from rest_framework import serializers
from crm_food.models import (
    Table, Role, Department, Status,
    ServicePercentage, MealCategory,
    Meal, Order, Check,
)


class TableSerializer(serializers.ModelSerializer):
   class Meta:
        model = Table
        fields = (
            'id',
            'name_of_tables',
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'name_of_roles',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name_of_departments',
        )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'id',
            'title',
        )


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = (
            'id',
            'service',
        )


class MealCategorySerializer(serializers.ModelSerializer):
    # departments_name = serializers.ReadOnlyField(source='department.name_of_departments')
    department = serializers.PrimaryKeyRelatedField(
            queryset = Department.objects.all()
    )
    departments_name = DepartmentSerializer(
        source='department',
        read_only=True,
        )
    class Meta:
        model = MealCategory
        fields = (
            'id',
            'title',
            'departments_name',
            'department',
        )

    # def create(self,)

class MealSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset = MealCategory.objects.all()
    )

    category_name = MealCategorySerializer(
        source='category',
        read_only=True,
    )
    # category_name = serializers.ReadOnlyField(source='category.title')
    class Meta:
        model = Meal
        fields = (
            'id',
            'name_of_meal',
            'price',
            'description',
            'category_name',
            'category',
        )


class OrderSerializer(serializers.ModelSerializer):
    table = serializers.PrimaryKeyRelatedField(
        queryset = Table.objects.all()
    )
    table_name = TableSerializer(
        source='table',
        read_only=True,
    )
    meal = serializers.SlugRelatedField(
        queryset= Meal.objects.all(),
        many=True,
        slug_field='name_of_meal',

    )
    meals_name = MealSerializer(
         source='meal',
         read_only=True,
         many=True,
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset = Status.objects.all()
    )
    status_name = StatusSerializer(
        source = 'status',
        read_only=True,

    )
    # table_name = serializers.ReadOnlyField(source='table.name_of_tables')
    # meal_name = serializers.ReadOnlyField(source='meal.name_of_meal')
    # status = serializers.ReadOnlyField(source='status.title')
    class Meta:
        model = Order
        fields = (
            'id',
            'isitopen',
            'date',
            'table',
            'table_name',
            'meal',
            'meals_name',
            'status',
            'status_name',
        )

    #
    # def create(self, validated_data):
    #     meals_data = validated_data.pop('meals')
    #     order = Order.objects.create(**validated_data)
    #     for meal_data in meals_data:
    #         Meal.objects.create(order=order, **meal_data)
    #     return order


class CheckSerializer(serializers.ModelSerializer):
    # service = serializers.ReadOnlyField(source='service.service')
    order = serializers.PrimaryKeyRelatedField(
        queryset = Order.objects.all()
    )
    order_name = OrderSerializer(
        source='order', #Значение source='*'
                        #имеет особое значение и используется для указания того, что весь объект должен быть передан в поле
        read_only=True #для чтения вложенных полей
    )
    service = serializers.PrimaryKeyRelatedField(
        queryset = ServicePercentage.objects.all()
    )
    service_percentage = ServicePercentageSerializer(
        source='service',
        read_only=True
    )
    class Meta:
        model = Check
        fields = (
            'id',
            'date',
            'total_sum',
            'service',
            'service_percentage',
            'order',
            'order_name',
        )
        # read_only_fields = ('order',)
