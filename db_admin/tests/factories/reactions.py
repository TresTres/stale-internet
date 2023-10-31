from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from db_admin.reactions import models as ReactionsModels

from db_admin.tests.factories.users import UserFactory


class ReactionCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ReactionsModels.ReactionCategory

    name = Faker("word")
    content = Faker("json")


class ReactionFactory(DjangoModelFactory):
    class Meta:
        model = ReactionsModels.Reaction

    creator = SubFactory(UserFactory)
    category = SubFactory(ReactionCategoryFactory)
    flavor_text = Faker("sentence")
    comment = None
    subject = None
    theme = None
