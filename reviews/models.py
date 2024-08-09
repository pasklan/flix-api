from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.PROTECT)
    stars = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 0 estrelas.'),
        ]
    )
    comment = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.movie)
