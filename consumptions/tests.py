from django.test import TestCase
from django.contrib.auth.models import User
from .models import Consumption


class ConsumptionTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')

        self.consumption = Consumption.objects.create()

    def test_add_users_to_consumption(self):
        self.consumption.user.add(self.user1, self.user2)
        self.assertEqual(len(self.consumption.user.all()), 2)

# ?????????
##########
# REVISAR
#######
