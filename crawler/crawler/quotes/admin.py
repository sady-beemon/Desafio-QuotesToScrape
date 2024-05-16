from django.contrib import admin
from crawler.quotes.models import Quotes
from crawler.quotes.actions import data_request


class AuthorFilter(admin.SimpleListFilter):
    title = ("Author da frase")
    parameter_name = "authorfilter"

    def lookups(self,request, model_admin):
        response = []
        for q in Quotes.objects.all():
            if (q.creator,q.creator) not in response:
                response.append((q.creator,q.creator))
        
        response.sort()
        return response
    
    def queryset(self, request, model_admin):
        for q in Quotes.objects.all():
            if self.value() == q.creator:
                return Quotes.objects.filter(
                    creator =(q.creator),
                    
                )

class BackgroundFix(admin.SimpleListFilter):
    title = ("Background_fix")
    parameter_name = "Background_fix"
    template = "background_color_fix.html"

    def lookups(self,request, model_admin):
        response = []
        for q in Quotes.objects.all():
            if (q.creator,q.creator) not in response:
                response.append((q.creator,q.creator))
        
        response.sort()
        return response
    
    def queryset(self, request, model_admin):
        for q in Quotes.objects.all():
            if self.value() == q.creator:
                return Quotes.objects.filter(
                    creator =(q.creator),
                    
                )


class QuotesAdmin(admin.ModelAdmin):
    list_display = ["content", "creator","tags"]
    ordering = ["content"]
    list_filter = [AuthorFilter,BackgroundFix]
    search_fields = ["content"]
    actions = ["fill_in"]
    change_form_template = 'quotes/custom_change_form.html'

    @admin.action(description="Fill in with data from https://quotes.toscrape.com/")
    def fill_in(modeladmin, request, queryset):
            data_request()

admin.site.register(Quotes, QuotesAdmin)

