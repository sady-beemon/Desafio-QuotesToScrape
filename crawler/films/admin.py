from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Movies


class YearFilterStart(admin.SimpleListFilter):
    title = _("Start Ano de Lançamento")
    parameter_name = "yearfilterstart"

    def lookups(self,request, model_admin):
        response = []
        for q in Movies.objects.all():
            if (q.date,q.date) not in response:
                response.append((q.date,q.date))
        
        response.sort()
        return response
     
    def queryset(self, request, model_admin):
        for q in Movies.objects.all():
            if q.date is not None and (str(self.value()) == str(q.date)):
                return Movies.objects.filter(
                    date=(q.date),

                )
            
class YearFilterEnd(admin.SimpleListFilter):
    title = _("End Ano de Lançamento")
    parameter_name = "yearfilterend"

    def lookups(self,request, model_admin):
        
        response = []
        for q in Movies.objects.all():
            if (q.date,q.date) not in response:
                response.append((q.date,q.date))
        
        response.sort()
        return response

    
    def queryset(self, request, model_admin):

        date_lte = request.GET.get('yearfilterstart',None)
        date_gte = request.GET.get('yearfilterend', None)
        if date_lte is not None and date_gte is not None :
            if request.GET.get('yearfilterstart') <= request.GET.get('yearfilterend'):
                return Movies.objects.filter(
                    date__gte = int(date_lte),
                    date__lte = int(date_gte),
                )

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
    list_filter = [YearFilterStart,YearFilterEnd,AgeFilter,ScoreFilter]
    search_fields = ['title'] 
    ordering = ["rank"]
    change_form_template = 'films/custom_change_form.html' 
    

admin.site.register(Movies, MovieAdmin)