from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import Movie,Actor,Albam,Track

from api.serializers import MovieSerializer,ActorSerializer,AlbamSerializer,TrackSerializer,ReviewSerializer

from rest_framework import viewsets

from rest_framework.decorators import action

class MovieListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        # logic for returning all movie

        qs=Movie.objects.all()

        serializer_instance=MovieSerializer(qs,many=True)#serialization

        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        # logic for adding movie

         #python native type=>qs

        serializer_instance=MovieSerializer(data=request.data) #deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    
class MovieRetriveUpdateDeleteView(APIView):

    def get(self,request,*args,**kwargs):

        # logic for returning movie detail

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(movie_obj,many=False)

        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):

        # logic for updating movie

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(data=request.data,instance=movie_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):

        # logic for delete movie

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})
    

class LanguageView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("language",flat=True).distinct()

        return Response(data=qs)
    
class GenreView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=qs)
    

class ActorViewSet(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serializer_instance=ActorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwargs):

        serializer_instance=ActorSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=serializer_instance.data)
    
    def update(self,request,*args,**Kwargs):

        id=Kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(data=request.data,instance=actor_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Actor.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})
    

class AlbamViewSetView(viewsets.ModelViewSet):

    serializer_class=AlbamSerializer

    queryset=Albam.objects.all()

    # custom method defined
    # url:localhost:8000/api/albams/languages
    # method:get

    @action(methods=["GET"],detail=False)
    def languages(self,request,*args,**kwargs):

        qs=Albam.objects.all().values_list("language",flat=True).distinct()

        return Response(data=qs)
    
    # url:localhost:8000/api/albams/directors/
    # method:GET 
    
    @action(methods=["GET"],detail=False)
    def directors(self,request,*args,**kwargs):

        qs=Albam.objects.all().values_list("director",flat=True).distinct()

        return Response(data=qs)

    # url:localhost:8000/api/albams/{id}/add_track
    # method:POST
    @action(methods=["POST"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        albam_object=Albam.objects.get(id=id)

        serializer_instance=TrackSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(albam_obj=albam_object)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

    @action(methods=["POST"],detail=True)   
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        albam_object=Albam.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(albam_obj=albam_object)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

        

# url:localhost:8000/api/tracks/{id}/

class TrackViewSetView(viewsets.ModelViewSet):

    serializer_class=TrackSerializer

    queryset=Track.objects.all()

    