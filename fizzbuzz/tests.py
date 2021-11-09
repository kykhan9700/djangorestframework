from django.test import TestCase
from django.conf import settings

from rest_framework.test import APITestCase

from fizzbuzz.models import FizzBuzz


class FizzbuzzCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_fizzbuzz_count = FizzBuzz.objects.count()
        fizzbuzz_attrs = {
            'fizzbuzz_id': 1,
            'message': 'Fizzbuzz 1',
            'creation_date': '2021-11-08T20:04:35.800840Z',
            'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    
        }
        response = self.client.post('/api/fizzbuzz/', fizzbuzz_attrs)
        if response.status_code != 201:
            print(response.data)
        # self.assertEqual(
        #     FizzBuzz.objects.count(),
        #     initial_fizzbuzz_count + 1,
        # )
        self.assertEqual(
            response.status_code,
            403,
        )

# class FizzbuzzListTestCase(APITestCase):
#     def test_list_fizzbuzz(self):
#         fizzbuzz_count = FizzBuzz.objects.count()
#         response = self.client.get('/api/fizzbuzz/')
#         print(response.data)
#         self.assertIsNone(response.data['next'])
#         self.assertIsNone(response.data['previous'])
#         self.assertEqual(response.data['count'], fizzbuzz_count)
#         self.assertEqual(len(response.data['results']), fizzbuzz_count)
# # Create your tests here.
