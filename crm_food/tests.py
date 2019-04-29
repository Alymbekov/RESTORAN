from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
        APITestCase,
)

from rest_framework.test import RequestsClient



class TestGetTable(APITestCase):


    def test_get_table(self):
        url = reverse('tables')
        response = self.client.get(url)
        print(response)
        print(' succesfully ')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class Test_Get_Table_By_Id(APITestCase):


    def test_get_table_by_id(self):
        """
        Проверяем get запрос по id на корректность
        """
        client = RequestsClient()
        response = client.get('http://localhost:9999/api/tables/2/')
        #response = self.client.get('/tables/1/')
        print(response)
        # assert response.status_code == HTTP_200_OK
        self.assertEqual(response.status_code,status.HTTP_200_OK)