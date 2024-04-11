from django.http import HttpResponseRedirect
from django.contrib import messages
from films.models import Movies
from bs4 import BeautifulSoup
import requests


def data_request_movie(request):

    URL='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser") 
    items_on_page = soup.find_all(class_ = "ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
    for items in items_on_page:
        data = []
        main = ((items.find(class_ = "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title")).get_text()).split(".",1)
        for objects in items.find_all(class_ = "sc-b0691f29-8 ilsLEX cli-title-metadata-item"):
            data.append(objects.get_text())
        
        if len(data) == 3:
            Movies.objects.get_or_create(
                rank = int(main[0]),
                title = (main[1]),
                date = int(data[0]),
                time = (data[1]),
                minage = (data[2]),
                score = items.find(class_ = "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").get_text().split('(',1)[0]
            )
        else:
            Movies.objects.get_or_create(
                rank = int(main[0]),
                title = (main[1]),
                date = int(data[0]),
                time = (data[1]),
                minage = ("Not Rated"),
                score = items.find(class_ = "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").get_text().split('(',1)[0]
            )
    messages.success(request,"Dados adicionados com sucesso.")
    return HttpResponseRedirect(request.headers['Referer'])