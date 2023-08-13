from rest_framework.serializers import ModelSerializer
from . import models

class SerializedMovies(ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'

class SerializedCustomer(ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class SerializedClient(ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class SerializedMovie(ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'