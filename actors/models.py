from django.db import models

NATIONALITY_CHOICES = (
    ('ARG', 'Argentina'),
    ('BOL', 'Bolívia'),
    ('BRA', 'Brasil'),
    ('COL', 'Colombia'),
    ('CHI', 'Chile'),
    ('EQU', 'Equador'),
    ('USA', 'Estados Unidos'),
    ('PAR', 'Paraguai'),
    ('PER', 'Peru'),
    ('URU', 'Uruguai'),
    ('VEN', 'Venezuela'),
)


class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
