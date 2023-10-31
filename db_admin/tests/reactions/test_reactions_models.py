import pytest

from django.core.exceptions import ValidationError

from tests.factories.reactions import ReactionFactory
from tests.factories.subjects import CommentFactory, SubjectFactory


@pytest.mark.django_db
class TestReactionModelLogic:
    def test_reaction_invalid_without_singular_target(self):
        reaction = ReactionFactory()
        with pytest.raises(ValidationError):
            reaction.clean()

        reaction = ReactionFactory(comment=CommentFactory(), subject=SubjectFactory())
        with pytest.raises(ValidationError):
            reaction.clean()
