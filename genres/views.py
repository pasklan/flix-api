from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from genres.serializers import GenreSerializer


class GenreCreateListView(ListCreateAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

