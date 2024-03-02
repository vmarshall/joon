from .models import Quest, DaysToRepeat
from rest_framework import serializers

class DaysToRepeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysToRepeat
        fields = "__all__"

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'description', 'date_created', 'date_completed', 'completed', 'repeats']

