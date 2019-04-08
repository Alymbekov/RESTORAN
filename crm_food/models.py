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
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Meal(models.Model):
    name_of_meal = models.CharField(max_length=100)
    category = models.ForeignKey('MealCategory', on_delete=models.SET_NULL, null=True)
    price = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name_of_meal


