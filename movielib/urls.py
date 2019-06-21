from django.urls import path
from . import views



app_name = 'movielib'  # here for namespacing of urls.

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("<int:vid>/video/", views.video1, name="video"),
    path("AddNewMovie/", views.AddNewMovie, name="AddNewMovie"),
    path("upload/", views.AddNewMovie, name="upload_movie"),
    path("<int:mid>/edit/", views.video_edit, name="video_edit"),
    path("<int:movId>/delete/", views.delete_movie, name="delete_movie"),


]