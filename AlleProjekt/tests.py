from django.test import TestCase
from .models import Locations

class ModelTest(TestCase):
    def setUp(self):
        self.location_name = "Gugle bugle"
        self.location = Locations(name = self.location_name)

    def test_can_create_model(self):
        old = Locations.objects.count()
        self.location.save()
        new = Locations.objects.count()
        self.assertNotEqual(old, new)