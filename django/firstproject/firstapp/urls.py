from django.conf.urls import url
from django.contrib import admin
from firstapp import views
from .views import scrape
from .views import index

#urlpatterns=[
    #url(r'^views/',scrape,name='scrape')
#]
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^views/',scrape,name='scrape'),
]
