from django.urls import path
from . import views

app_name = 'movieapp'
# Name space remove the conflict of differentapp 'name' (naming issue) .
urlpatterns = [

    # path('', views.hello, name="hello"),
    path('', views.movie, name="movie"),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('movielink', views.movie_link, name="movielink"),
    path('add/', views.add_movie, name='addmovie'),
    path('edit/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
