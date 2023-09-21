from factory import Faker, SubFactory, LazyFunction
from factory.django import DjangoModelFactory

from db_admin.subjects import models as SubjectModels
from tests.factories.themes import ThemeFactory
from tests.factories.users import UserFactory

class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = SubjectModels.Subject

    title = Faker("sentence")
    description = Faker("paragraph")
    theme = SubFactory(ThemeFactory)
    author = SubFactory(UserFactory)
    timestamp = Faker("date_time")
    
    
class CommentFactory(DjangoModelFactory):
    class Meta:
        model = SubjectModels.Comment
        
    author = SubFactory(UserFactory)
    original_subject = SubFactory(SubjectFactory)
    parent_comment = LazyFunction(lambda: CommentFactory(previous_comment=None, parent_comment=None))
    previous_comment = LazyFunction(lambda: CommentFactory(previous_comment=None, parent_comment=None))
    text_content = Faker("paragraph")
    timestamp = Faker("date_time")
    