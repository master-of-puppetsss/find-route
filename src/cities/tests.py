from django.db import DataError, IntegrityError
from django.test import TestCase

from cities.models import City


class CityModelTest(TestCase):
    def setUp(self):
        super().setUp()
        self.city = City.objects.create(
            name='Amsterdam'
        )

    def test_name_max_length(self):
        self.city.name = 'a' * 101
        with self.assertRaises(DataError):
            self.city.save()

    def test_name_label(self):
        verbose = self.city._meta.get_field('name').verbose_name
        self.assertEqual(verbose, 'Название города')

    def test_name_unique(self):
        with self.assertRaises(IntegrityError):
            City.objects.create(name='Amsterdam')

    def test_name_str(self):
        self.assertEqual(str(self.city), self.city.name)

