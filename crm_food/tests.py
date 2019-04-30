import json
import unittest
from .models import *
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
                            APITestCase,
                            RequestsClient,
                            APIRequestFactory,
                            APIClient,
                        )

class TestCreateTable(APITestCase):
    def setUp(self):
        self.table = Table(name_of_tables='table1',)
        self.table.save()


    def test_table_creation(self):
        response = self.client.post(reverse('tables'), {
            'name_of_tables': 'table 2',
        })
        print(response)
        #assert was movie added
        self.assertEqual(Table.objects.count(), 2)
        #assert created status code was returned
        self.assertEqual(201, response.status_code)


    def test_getting_tables(self):
        response = self.client.get(reverse('tables'), format="json")
        # print(response.data.keys())
        self.assertEqual(len(response.data), 1)


    def test_updating_table(self):
        response = self.client.put(reverse('details', kwargs={'pk':self.table.id}), {
            'name_of_tables': 'table 1 updated',
            }, format="json")
        response = response.json()
        self.assertEqual('table 1 updated', response['name_of_tables'])


    def test_deleting_tables(self):
        response = self.client.delete(reverse('details', kwargs={'pk': self.table.id}))
        self.assertEqual(204, response.status_code)



class TestCreateRole(APITestCase):
    def setUp(self):
        self.role = Role(name_of_roles='Waiter')
        self.role.save()


    def test_role_creation(self):
        response = self.client.post(reverse('roles'), {
            'name_of_roles': 'Administrator'
        })
        self.assertEqual(Role.objects.count(), 2)
        #assert created status code was returned
        self.assertEqual(201, response.status_code)


    def test_getting_roles(self):
        response = self.client.get(reverse('roles'), format='json')
        self.assertEqual(len(response.data), 1)


    def test_updating_role(self):
        response = self.client.put(reverse('roles_detail', kwargs={'pk':self.role.id}), {
            'name_of_roles': 'waiter updated',
            }, format="json")
        response = response.json()
        self.assertEqual('waiter updated', response['name_of_roles'])


    def test_deleting_role(self):
        response = self.client.delete(reverse('roles_detail', kwargs={'pk':self.role.id}))
        self.assertEqual(204, response.status_code)


class TestCreateDepartment(APITestCase):
    def setUp(self):
        self.department = Department(name_of_departments='Bar')
        self.department.save()


    def test_department_creation(self):
        response = self.client.post(reverse('departments'), {
            'name_of_departments': 'Bar'
        })
        self.assertEqual(Department.objects.count(), 2)
        #assert created status code was returned
        self.assertEqual(201, response.status_code)



    def test_getting_department(self):
        response = self.client.get(reverse('departments'), format='json')
        self.assertEqual(len(response.data), 1)


    def test_updating_department(self):
        response = self.client.put(reverse('departments_detail', kwargs={'pk': self.department.id}), {
            'name_of_departments': "updated department"
        }, format='json')
        response = response.json()
        self.assertEqual('updated department', response['name_of_departments'])


    def test_deleting_department(self):
        response = self.client.delete(reverse('departments_detail', kwargs={'pk': self.department.id}))
        self.assertEqual(204, response.status_code)


class TestCreateStatus(APITestCase):
    def setUp(self):
        self.status = Status(title='in progress')
        self.status.save()


    def test_status_creation(self):
        response = self.client.post(reverse('statuses'), {
            'title': 'done'
        })
        self.assertEqual(Status.objects.count(), 2)
        #assert created status code was returned
        self.assertEqual(201, response.status_code)



    def test_getting_status(self):
        response = self.client.get(reverse('statuses'), format='json')
        self.assertEqual(len(response.data), 1)


    def test_updating_department(self):
        response = self.client.put(reverse('statuses_detail', kwargs={'pk': self.status.id}), {
            'title': "updated status"
        }, format='json')
        response = response.json()
        self.assertEqual('updated status', response['title'])


    def test_deleting_department(self):
        response = self.client.delete(reverse('statuses_detail', kwargs={'pk': self.status.id}))
        self.assertEqual(204, response.status_code)


class TestCreateServicePercentage(APITestCase):
        def setUp(self):
            self.service = ServicePercentage(service=25)
            self.service.save()


        def test_service_creation(self):
            response = self.client.post(reverse('services'), {
                'service': 50
            })
            self.assertEqual(ServicePercentage.objects.count(), 2)
            #assert created status code was returned
            self.assertEqual(201, response.status_code)


        def test_getting_services(self):
            response = self.client.get(reverse('services'), format='json')
            self.assertEqual(len(response.data), 1)


        def test_updating_services(self):
            response = self.client.put(reverse('services_detail', kwargs={'pk': self.service.id}), {
                'service': 75
            }, format='json')
            response = response.json()
            self.assertEqual(75, response['service'])


        def test_deleting_services(self):
            response = self.client.delete(reverse('services_detail', kwargs={'pk': self.service.id}))
            self.assertEqual(204, response.status_code)
