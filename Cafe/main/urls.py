from django.urls import path
from . import views

urlpatterns = [
path("menu/<str:item>", views.name, name="itemname"),
path("menu",views.menu,name="menu"),
path('about_us/', views.about_us, name='about_us'),
path('contact_us/', views.contact_us, name='contact_us'),
path("place_order/", views.place_order, name="place_order"),  # Define the new URL pattern here
path("",views.home,name='home'),
path("home/", views.home, name='home'),

]