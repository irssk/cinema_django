from django.db import models
from django.utils.text import slugify


class Movies(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'

class Ticket(models.Model):
    movie_title = models.OneToOneField(Movies, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

class Customer(models.Model):
    user_name = models.CharField(max_length=50)
    tickets = models.ManyToManyField(Ticket)
    number_of_tickets = models.IntegerField(null=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Places(models.Model):
    number = models.IntegerField()
    owner = models.OneToOneField(Ticket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'


