from django.shortcuts import render, redirect
# Create your views here.
from .models import Movie
from .forms import MovieForm

"""def hello(request):

    return HttpResponse("Welcome swapna")"""


def movie(request):
    movie_details = Movie.objects.all()
    context = {
        'movie_key': movie_details
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    # return HttpResponse("Movie id is: %s" % movie_id)
    movie_all_details = Movie.objects.get(id=movie_id)
    return render(request, 'movielink.html', {'movielink1': movie_all_details})


def movie_link(request):
    movie_data = Movie.objects.all()
    return render(request, 'detail_movie.html', {'movie_datakey': movie_data})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        # syntaxUse the MultiValueDict's get method. This is also present on standard dicts and is a way to fetch a value while providing a default if it does not exist.
        # is_private = request.POST.get('is_private', False)
        # Generally,my_var = dict.get(<key>, <default>)
        year = request.POST.get('year', )
        image = request.FILES['image']
        movie1 = Movie(name=name, description=description, image=image, year=year)
        movie1.save()

    return render(request, 'addmovie.html')


def update(request, id):
    movie_var = Movie.objects.get(id=id)
    movie_form_var = MovieForm(request.POST or None, request.FILES, instance=movie_var)
    if movie_form_var.is_valid():
        movie_form_var.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie_form_key': movie_form_var, 'movie_var_key': movie_var})


def delete(request, id):
    if request.method == 'POST':
        movie_var1 = Movie.objects.get(id=id)
        movie_var1.delete()
        return redirect('/')
    return render(request, 'delete.html')
