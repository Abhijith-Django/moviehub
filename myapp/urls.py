from django.urls import path

from myapp import views

urlpatterns=[

    path('movies/all/',views.MovieListView.as_view(),name="movie-list"),
    path('movies/add/',views.MovieCreateView.as_view(),name="movie-create"),
    path('movies/<int:pk>/',views.MovieDetailView.as_view(),name="movie-detail"),
    path('movie/<int:pk>/remove',views.MovieDeleteView.as_view(),name="movie-delete"),
    path('movies/<int:pk>/change',views.MovieUpdateView.as_view(),name="movie-update"),
]