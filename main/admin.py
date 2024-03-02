# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Quest, DaysToRepeat

class DaysToRepeatInline(admin.TabularInline):
    model = DaysToRepeat
    extra = 1  # Number of extra forms displayed
    fields = (
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    )

    raw_id_fields = ('quest',)
    can_delete = True
    view_on_site = True
    show_change_link = True
    show_url = True

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    inlines = [DaysToRepeatInline]
    list_display = (
        'id',
        'title',
        'repeats',
        'description',
        'date_created',
        'date_completed',
        'completed',
    )
    list_display_links = ('id', 'title')
    list_filter = ('date_created', 'date_completed', 'completed')
    search_fields = ('title',)
@admin.register(DaysToRepeat)
class DaysToRepeatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'quest',
        'get_repeats_by_day',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    )
    list_filter = (
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    )
    search_fields = ('quest__title',)
    autocomplete_fields = ('quest',)

#