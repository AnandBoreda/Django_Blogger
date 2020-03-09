from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
     path('', HomePageView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('index.html', HomePageView.as_view(), name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('single.html', views.single, name='single'),
    path('lifestyle.html',views.lifestyle, name='lifestyle'),
    path('health.html',views.health, name='health'),
    path('family.html',views.family, name='family'),
    path('technology.html',views.technology, name='technology'),
    path('travel.html',views.travel, name='travel'),
    path('work.html',views.work, name='work'),
]
