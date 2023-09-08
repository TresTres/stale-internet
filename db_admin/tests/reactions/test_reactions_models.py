from django.core.exceptions import ValidationError
import pytest
from tests.factories.reactions import ReactionFactory


@pytest.mark.django_db
class TestReactionModelLogic:

    def test_reaction_invalid_without_target(self):
        reaction = ReactionFactory() 
        with pytest.raises(ValidationError):
            reaction.clean()