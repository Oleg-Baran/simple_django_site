from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'), #Call views for look index (main page)
    path('about', views.about, name='about'),
]