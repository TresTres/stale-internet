from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from db_admin.themes import models as ThemeModels

from db_admin.tests.factories.users import UserFactory


class ThemeFactory(DjangoModelFactory):
    class Meta:
        model = ThemeModels.Theme

    creator = SubFactory(UserFactory)
    title = Faker("sentence")
    description = Faker("sentence")
