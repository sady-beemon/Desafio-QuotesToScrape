from django.contrib import admin
from quotes.models import Quotes
from quotes.actions import data_request, single_request



class QuotesAdmin(admin.ModelAdmin):
    list_display = ["content", "creator","tags"]
    ordering = ["content"]
    actions = ["fill_in"]

    @admin.action(description="Fill in with data from https://quotes.toscrape.com/")
    def fill_in(modeladmin, request, queryset):
            data_request()

    #@admin.action(description="WIP - Fill selected with data from https://quotes.toscrape.com/")
    #def fill_in_selected(modeladmin, request, queryset):
            #single_request()

admin.site.register(Quotes, QuotesAdmin)

# Register your models here.
 