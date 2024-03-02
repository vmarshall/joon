import json
from datetime import datetime
from django.db import models
from django.http import JsonResponse

DAYS_OF_WEEK = (
    ('MON', ('Monday')),
    ('TUE', ('Tuesday')),
    ('WED', ('Wednesday')),
    ('THU', ('Thursday')),
    ('FRI', ('Friday')),
    ('SAT', ('Saturday')),
    ('SUN', ('Sunday')),
)
class Quest(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def repeats(self):
        quest = DaysToRepeat.objects.filter(quest=self)
        print(f"quest: {quest}")
        result = ''
        for q in quest:
            print(f"q: {q}")
            result += f"{q}"


        # return JsonResponse({"repeats":data})
        return result

    def serialize_as_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'description': self.description,
            'date_completed': self.date_completed,
            'repeats': self.repeats(),
        }

    def __str__(self):
        return self.title

class DaysToRepeat(models.Model):

    quest = models.OneToOneField(Quest, on_delete=models.CASCADE, related_name='days_to_repeat')
    monday = models.BooleanField(default=False, help_text="Repeat on Monday")
    tuesday = models.BooleanField(default=False, help_text="Repeat on Tuesday")
    wednesday = models.BooleanField(default=False, help_text="Repeat on Wednesday")
    thursday = models.BooleanField(default=False, help_text="Repeat on Thursday")
    friday = models.BooleanField(default=False, help_text="Repeat on Friday")
    saturday = models.BooleanField(default=False, help_text="Repeat on Saturday")
    sunday = models.BooleanField(default=False, help_text="Repeat on Sunday")




    def get_repeats_by_day(self):

        repeat_days = []
        if self.monday:
            repeat_days.append('Monday')
        if self.tuesday:
            repeat_days.append('Tuesday')
        if self.wednesday:
            repeat_days.append('Wednesday')
        if self.thursday:
            repeat_days.append('Thursday')
        if self.friday:
            repeat_days.append('Friday')
        if self.saturday:
            repeat_days.append('Saturday')
        if self.sunday:
            repeat_days.append('Sunday')
        return repeat_days


    # def repeats_on_date(self, date):
    #     weekday = date.weekday()
    #     print(f"self: {self}")
    #     print(f"date: {date}")
    #     print(f"weekday: {date.weekday()}")
    #     if weekday == 0:
    #         return self.monday
    #     elif weekday == 1:
    #         return self.tuesday
    #     elif weekday == 2:
    #         return self.wednesday
    #     elif weekday == 3:
    #         return self.thursday
    #     elif weekday == 4:
    #         return self.friday
    #     elif weekday == 5:
    #         return self.saturday
    #     elif weekday == 6:
    #         return self.sunday
    #     else:
    #         return False

    def __str__(self):
        return ', '.join(self.get_repeats_by_day())
