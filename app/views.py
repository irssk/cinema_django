from . import models
from .models import Movies, Customer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def see_all_movies(request):
    movies = Movies.objects.all()
    serialized_movies = SerializedMovies(movies, many=True)
    data = serialized_movies.data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def see_one_movie(request, slug):
    movie = Movies.objects.get(slug=slug)
    serialized_movie = SerializedMovie(movie)
    data = serialized_movie.data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def see_all_customers(request):
    customers = Customer.objects.all()
    serialized_customers = SerializedCustomer(customers, many=True)
    data = serialized_customers.data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def see_one_customer(request, slug):
    client = Customer.objects.get(slug = slug)
    serialized_client = SerializedClient(client)
    data = serialized_client.data
    return Response(data, status=status.HTTP_200_OK)








