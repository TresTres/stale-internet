from rest_framework import serializers

from db_admin.reactions.models import Reaction, ReactionCategory


class ReactionCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReactionCategory
        fields = '__all__'

class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'
        