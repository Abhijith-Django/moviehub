from rest_framework import serializers

from myapp.models import Movie,Actor,Albam,Track,Review

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model=Movie

        fields="__all__"


class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:

        model=Actor

        fields="__all__"

class TrackSerializer(serializers.ModelSerializer):

    albam_obj=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Track

        fields="__all__"

        read_only_fields=["id","albam_obj"]

class ReviewSerializer(serializers.ModelSerializer):

    albam_obj=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=["id","created_date","albam_obj"]

class AlbamSerializer(serializers.ModelSerializer):

    songs=TrackSerializer(many=True,read_only=True)#nested serializer(a serializer in another serializer)

    songs_count=serializers.CharField(read_only=True)

    reviews=ReviewSerializer(many=True,read_only=True)

    avg_rating=serializers.CharField(read_only=True)

    reviews_count=serializers.CharField(read_only=True)

    class Meta:

        model=Albam

        fields=["id","title","year","director","language","songs_count","songs","reviews_count","avg_rating","reviews"]


 