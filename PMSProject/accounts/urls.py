from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('buying', views.buying, name="buying"),
    path('selling', views.selling, name="selling"),
    path('contacts', views.contacts, name="contacts"),

]