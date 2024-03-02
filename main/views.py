import json
import logging
from pprint import pprint

from django.http import JsonResponse
from datetime import datetime

from main.models import Quest, DaysToRepeat

logging.basicConfig(level=logging.DEBUG)

def create_quest(request):
    post_params = json.loads(request.body.decode('utf-8'))
    title = post_params.get('title')
    description = post_params.get('description')

    # repeats_information is an array of 7 Booleans where each Boolean represents
    # whether it should repeat on a given day of the week (Monday
    # being index 0).  It can also be None if it doesn’t repeat.
    repeats_information = post_params.get('repeats_information')

    quest = Quest.objects.create(title=title, description=description, completed=False)

    if repeats_information is not None:
        pattern = DaysToRepeat(
            quest=quest,
            monday=repeats_information[0],
            tuesday=repeats_information[1],
            wednesday=repeats_information[2],
            thursday=repeats_information[3],
            friday=repeats_information[4],
            saturday=repeats_information[5],
            sunday=repeats_information[6]
        )
        pattern.save()

    # [Your code here] Create the Quest here.
    quest = Quest.objects.first()
    return JsonResponse({'quest': quest.serialize_as_json()})


def get_quests(request):

    date_string = request.GET.get('date',  datetime.now().strftime('%Y-%m-%d'))
    date = datetime.strptime(date_string, '%Y-%m-%d')
    logging.debug(date)
    quests = []
    all_quests = Quest.objects.filter(completed=False, days_to_repeat__isnull=True)
    for quest in all_quests:
        logging.debug(quest)
        print(f"quest: {quest}")
        print(f"repeats: {quest.repeats()}")
        print(f"today's date: {date.date()}")
        # has_repeat_pattern = DaysToRepeat.objects.filter(quest=quest).exists()
        # print(f"has_repeat_pattern: {has_repeat_pattern}")
        # if quest.date_completed and quest.date_completed.date() == date.date():
        #     quest.completed = True
        # elif quest.repeatpattern_set.exists():
        #     repeat_pattern = quest.repeatpattern_set.first()
        #     if repeat_pattern.repeats_on_date(date):
        #         quest.completed = True
        #     else:
        #         quest.completed = False
        # else:
        #     quest.completed = False
        # quests.append(quest)

    # quests = Quest.objects.all()
    return JsonResponse({'quests': [quest.serialize_as_json() for quest in all_quests]})

def get_completed_quests(request):
    logging.debug("get_completed_quests")
    all_quests = Quest.objects.filter(completed=True)
    for quest in all_quests:
        logging.debug(quest)
        print(f"quest: {quest}")

    return JsonResponse({'quests': [quest.serialize_as_json() for quest in all_quests]})


def get_repeating_quests(request):
    logging.debug("get_completed_quests")
    all_quests = Quest.objects.filter(days_to_repeat__isnull=False).exclude(date_completed__isnull=False)
    # all_quests.exclude(date_completed__isnull=True)
    for quest in all_quests:
        print(f"quest: {quest}")

    return JsonResponse({'quests': [quest.serialize_as_json() for quest in all_quests]})
