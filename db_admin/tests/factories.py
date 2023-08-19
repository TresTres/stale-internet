from factory import DjangoModelFactory, Faker

from django.contrib.auth.models import User 

from themes import models as ThemeModels
from subjects import models as SubjectModels
from reactions import models as ReactionModels


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("name")
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

class ThemeFactory(DjangoModelFactory):
    class Meta:
        model = ThemeModels.Theme

    creator = UserFactory()
    title = Faker("sentence")
    description = Faker("sentence")

        
class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = SubjectModels.Subject

    title = Faker("sentence")
    description = Faker("paragraph")
    theme = ThemeFactory()
    author = UserFactory()
    timestamp = Faker("date_time")
    
    
    
