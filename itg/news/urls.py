from django.urls import path
from .views import  get_news_by_id, news_catalog,catalog, get_category_by_name, main,get_detail_article_by_id

urlpatterns = [
    # path('catalog', news_catalog, name='catalog'),
    # path('<int:news_id>/', get_news_by_id, name='get_news_by_id'),
    path('', main, name='index'),
    path('catalog/', news_catalog, name='catalog'),
    path('catalog/<slug:slug>/', get_category_by_name, name='get_category_by_name'),
    path('catalog/<int:article_id>/', get_news_by_id, name='get_news_by_id'),
]
