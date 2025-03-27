from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
articles = [
    {'id':1,'title':'First News', 'summary':'Краткое описание первой новости.'},
    {'id':2, 'title': 'Second News', 'summary':'Краткое описание second новости.'}
]
def main(request):
    return render(request, 'main.html')

def get_news_by_id(request,article_id):
    return HttpResponse(f'News {article_id}')

def news_catalog(request):
    return render(request, 'news/catalog.html', {'articles': articles} )

def catalog(request):
    return HttpResponse('Каталог новостей')

def get_category_by_name(request, slug):
    return HttpResponse(f'Категория {slug}')
def get_detail_article_by_id(request, article_id):
    article = next((news for news in articles if news["id"] == article_id), None)

    if article:
        return render(request, 'news/article_detail.html', {'article': article})
    else:
        return HttpResponseNotFound("<h1>Статья не найдена</h1>")