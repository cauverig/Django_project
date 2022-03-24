from movieapi.serializers import MovieSerializer
from django.shortcuts import render
from rest_framework import generics
from movie.models import Movie
from .serializers import MovieSerializer
# Create your views here.

class MovieAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer