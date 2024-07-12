from django.db import models

# Create your models here.

from django.db.models import Avg


class Movie(models.Model):

    title=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    language=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    producer=models.CharField(max_length=200,null=True)

    def __str__(self):
        
        return self.title

class Actor(models.Model):

    name=models.CharField(max_length=200)

    age=models.PositiveIntegerField()

    picture=models.ImageField(upload_to="image",null=True)

    gender_option=(
        ("male","male"),
        ("female","female")
    )

    gender=models.CharField(max_length=200,choices=gender_option,default="male")


    def __str__(self):
        return self.name
    

class Albam(models.Model):

    title=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    year=models.CharField(max_length=200)
    
    @property
    def songs(self):

        qs=Track.objects.filter(albam_obj=self)

        return qs
    

    @property
    def songs_count(self):

        qs=Track.objects.filter(albam_obj=self).count()

        return qs

    def __str__(self):
        return self.title
    
    @property
    def reviews(self):

        qs=Review.objects.filter(albam_obj=self)

        return qs
    
    @property
    def reviews_count(self):

        return self.reviews.count()
    
    @property
    def avg_rating(self):

        all_reviews=self.reviews

        avg=all_reviews.values("rating").aggregate(avg=Avg("rating"))["avg"]

        return round(avg,1) if avg else avg

    
    

class Track(models.Model):

    title=models.CharField(max_length=200)

    duration=models.CharField(max_length=200)

    track_number=models.PositiveIntegerField(default=1)

    singers=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    albam_obj=models.ForeignKey(Albam,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Review(models.Model):

    comment=models.CharField(max_length=200)

    rating=models.PositiveIntegerField()

    user=models.CharField(max_length=200)

    created_date=models.DateTimeField(auto_now_add=True)

    albam_obj=models.ForeignKey(Albam,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment




