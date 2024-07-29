from django.http import HttpResponseRedirect
import json
from django.contrib import messages
from crawler.films.models import Movies
from bs4 import BeautifulSoup
import requests

def run_crawler_IMDb(request):

    filmes_json, timelist_filmes = data_request_movie()
    update_movies(filmes_json,timelist_filmes,request)

def data_request_movie():

    URL='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser") 
    filmes_json = json.loads(soup.find('script', type='application/json').text)
    filmes_timelist_json = json.loads(soup.find('script', type='application/ld+json').text)
    timelist = []

    for filme_extra in filmes_timelist_json['itemListElement']:
        timelist.append(filme_extra['item']['duration'].split('PT',1)[1])

    return filmes_json,timelist


def update_movies(filmes_json, timelist, request):
    
    for index,filme in enumerate(filmes_json["props"]["pageProps"]['pageData']['chartTitles']['edges']):

    
        node = filme.get("node")
        filme_name = ''
        consentAge = "Not Rated"

        if node:
            certificate = node.get('certificate')
            titleText = node.get("titleText")
            originaltitleText = node.get("originaltitleText")
            
            if titleText:
                filme_name = filme["node"]["titleText"]["text"]
            elif originaltitleText:
                filme_name = filme["node"]["originaltitleText"]["text"]

            if certificate:
                if certificate.get("rating"):
                    consentAge = filme["node"]["certificate"]["rating"]

        Movies.objects.get_or_create(
            rank = int(filme['currentRank']),
            title = filme_name,
            date = int(filme['node']['releaseYear']['year']),
            time = timelist[index],
            minage = consentAge,
            score = float(filme['node']["ratingsSummary"]["aggregateRating"])
        )
        
    messages.success(request,"Filems atualizados com sucesso.")
    return HttpResponseRedirect(request.headers['Referer'])