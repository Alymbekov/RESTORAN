from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


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
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    count = models.ManyToManyField('Meal', through='CountMeals', related_name='orders_count')
    total_sum = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{} + {} + {} + {}+{}'.format(self.table, self.isitopen, self.meal, self.status, self.count)

    def total_sum(self):
        self.total_sum = "12"+ str(self.count)
        return self.total_sum
    # totall_sum = []
    # count = 5
    # def total_sum(self, count):
    #     if self.count == self.count:
    #         for x in range(1,self.count+1):
    #             self.totall_sum.append(self.meal.price)
    #     return sum(totall_summ)
    # print(totall_sum)

class CountMeals(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='countmeal')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='countmeal')
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{},{},{}'.format(self.meal, self.order, self.count)


class Check(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    service = models.ForeignKey('ServicePercentage', on_delete=models.CASCADE, null=True)
    total_sum = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s' % self.order


# class User(AbstractUser):
#     username = models.CharField(max_length=255,blank=True, null=True)
#     email = models.EmailField(_('email address'), unique=True)
#     role = models.OneToOneField('Role', on_delete=models.CASCADE, null=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#
#     def __str__(self):
#         return "{}".format(self.email)
