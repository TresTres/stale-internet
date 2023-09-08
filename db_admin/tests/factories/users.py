from factory import Faker
from factory.django import DjangoModelFactory

from django.contrib.auth.models import User 


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("name")
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
