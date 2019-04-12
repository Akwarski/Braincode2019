from django.test import TestCase
from .models import Paczkomat

class ModelTest(TestCase):
    def setUp(self):
        self.Paczkomat_name = "Gugle bugle"
        self.Paczkomat = Paczkomat(name = self.Paczkomat_name)

    def test_can_create_model(self):
        old = Paczkomat.objects.count()
        self.Paczkomat.save()
        new = Paczkomat.objects.count()
        self.assertNotEqual(old, new)
# Create your tests here.
