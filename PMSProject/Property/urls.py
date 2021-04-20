from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('buying', views.buying, name="buying"),
    path('selling', views.selling, name="selling"),
    path('contacts', views.contacts, name="contacts"),

]