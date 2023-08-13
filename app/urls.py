from django.urls import path
from .views import see_all_movies, see_one_movie, see_all_customers, see_one_customer

urlpatterns = [
   path('movies/', see_all_movies, name='movies'),
   path('movies/<slug:slug>', see_one_movie, name="<slug>"),
   path('customers/', see_all_customers, name="customers"),
   path('customers/<slug:slug>', see_one_customer, name="<slug>"),
]

