from unittest import TestCase
from django.test import Client


class TestMobileResumeUpload(TestCase):
    def setUp(self):
        self.client = Client()
