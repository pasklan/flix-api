from django.db.models import Count, Avg
from movies.models import Movie
from movies.serializers import MovieSerializer, MoviewDetailSerializaser
from rest_framework import generics, views, response, status
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviewDetailSerializaser
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStasView(views.APIView):
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_stars': average_stars
            },
            status=status.HTTP_200_OK,
        )
