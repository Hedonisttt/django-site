
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('supp', views.supp, name='supp'),
    path('create', views.create, name='create')

]
