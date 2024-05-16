from django.http import HttpResponseRedirect
from django.contrib import messages
from crawler.films.models import Movies
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
        main = ((items.find(class_ = "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title")).get_text()).split(".",1)
        
        for objects in items.find_all(class_ = "sc-b189961a-8 kLaxqf cli-title-metadata-item"):
            data.append(objects.get_text())
            rawscore = items.find(class_ = "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").get_text().split('(',1)[0]
            rawscore = rawscore.replace(',','.')
            rawscore = ''.join(rawscore)

        if len(data) == 3:
            Movies.objects.get_or_create(
                rank = int(main[0]),
                title = (main[1]),
                date = int(data[0]),
                time = (data[1]),
                minage = (data[2]),
                score = float(rawscore)
            )
        else:
            Movies.objects.get_or_create(
                rank = int(main[0]),
                title = (main[1]),
                date = int(data[0]),
                time = (data[1]),
                minage = ("Not Rated"),
                score = float(rawscore)
            )

    messages.success(request,"Dados adicionados com sucesso.")
    return HttpResponseRedirect(request.headers['Referer'])