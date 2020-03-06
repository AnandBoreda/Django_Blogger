from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('registration.html', views.registration, name='registration'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    path('login.html', views.login, name='login'),
    path('services.html', views.services, name='services'),
    path('single.html', views.single, name='single'),
]
