from collections.abc import Iterator
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from .models import Movies

def get_range_date(value):
    start_date = None
    end_date = None

    if value:
        start_date, end_date = value.split(' - ')
        start_date = int(start_date)
        end_date = int(end_date)

    return start_date, end_date


class InputRangeDateFilter(SimpleListFilter):
    template = 'input_range_filter.html'

    def lookups(self, *_):
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v) for k, v in changelist.get_filters_params().items() if k != self.parameter_name
        )
        yield all_choice


def DateRangeFilter(date_field_name, title):
    range_filter = InputRangeDateFilter
    range_filter = type(f'{date_field_name.capitalize()}InputRangeDateFilter', (range_filter,), {})

    range_filter.parameter_name = f'{date_field_name}_range'
    range_filter.title = title

    def queryset(self, _, queryset):
        start_date, end_date = get_range_date(self.value())

        if start_date and end_date:
            gte_lte = {
                f'{date_field_name}__gte': start_date,
                f'{date_field_name}__lte': end_date,
            }

            queryset = queryset.filter(**gte_lte)

        return queryset

    range_filter.queryset = queryset

    return range_filter


class AgeFilter(admin.SimpleListFilter): 
    title = _("Idade minima")
    parameter_name = "agefilter"

    def lookups(self,request, model_admin):
        response = [] 
        for q in Movies.objects.all():
            if (q.minage,q.minage) not in response:
                response.append((q.minage,q.minage))
        
        response.sort( )
        return response
     
    def queryset(self, request, model_admin):
        for q in Movies.objects.all():
            if self.value() == q.minage:
                return Movies.objects.filter(
                    minage=(q.minage),
                )

class ScoreFilter(admin.SimpleListFilter): 
    title = _("Nota do filme")
    parameter_name = "scorefilter"

    def lookups(self,request, model_admin):
        response = []
        for q in Movies.objects.all(): 
            if (q.score,q.score) not in response:
                response.append((q.score,q.score))
        
        response.sort(reverse=True)
        return response
     
    def queryset(self, request, model_admin):
        for q in Movies.objects.all():
            if self.value() == q.score:
                return Movies.objects.filter(
                    score=(q.score),
                )

class MovieAdmin(admin.ModelAdmin):
    list_display = ["rank", "title","date","time","minage","score"]
    list_filter = [DateRangeFilter('date', 'Criado: de - até'),AgeFilter,ScoreFilter]
    search_fields = ['title'] 
    ordering = ["rank"]
    change_form_template = 'films/custom_change_form.html' 
    

admin.site.register(Movies, MovieAdmin)