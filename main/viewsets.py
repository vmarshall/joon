from rest_framework.viewsets import ModelViewSet

from main.models import Quest, DaysToRepeat
from main.serializers import QuestSerializer, DaysToRepeatSerializer
from rest_framework import permissions


class QuestViewSet(ModelViewSet):
    """
    API endpoint that allows quests to be viewed or edited.
    """
    queryset = Quest.objects.all().order_by('-date_created')
    serializer_class = QuestSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return self.request.quests.all()


class DaysToRepeatViewSet(ModelViewSet):
    """
    API endpoint that allows DaysToRepeat to be viewed or edited.
    """
    queryset = DaysToRepeat.objects.all()
    serializer_class = DaysToRepeatSerializer
    permission_classes = [permissions.IsAuthenticated]