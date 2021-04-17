from django.db import models

# Create your models here.
class Movie(models.Model):
    _id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    rating = models.IntegerField()


    def __str__(self):
        return self.name

class Gerne(models.Model):
    _id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie_Gerne(models.Model):
    _id = models.AutoField(primary_key=True, null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    gerne_id = models.ForeignKey(Gerne, on_delete=models.CASCADE)