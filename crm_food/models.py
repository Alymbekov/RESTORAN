from django.db import models


class Table(models.Model):
    name_of_tables = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_tables


class Role(models.Model):
    name_of_roles = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_roles


class Department(models.Model):
    name_of_departments = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_departments


class MealCategory(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey('Department', related_name='mealcategories', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Meal(models.Model):
    name_of_meal = models.CharField(max_length=100)
    category = models.ForeignKey('MealCategory',related_name='meals', on_delete=models.SET_NULL, null=True)
    price = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name_of_meal


class Status(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class ServicePercentage(models.Model):
    service = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s' % self.service


class Order(models.Model):
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    isitopen = models.PositiveSmallIntegerField()
    meal = models.ManyToManyField('Meal', related_name='orders')
    status = models.OneToOneField('Status', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{} + {} + {} + {}'.format(self.table, self.isitopen, self.meal, self.status)


class Check(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    service = models.ForeignKey('ServicePercentage', on_delete=models.CASCADE, null=True)
    total_sum = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s' % self.order

