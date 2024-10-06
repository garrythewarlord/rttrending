from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout

from script import main_parser
from .models import new_tv_show, best_tv_show, new_movie, best_movie

from django.db.models import F

from .helpers import create_instance

# Create your views here.



def main(request):
    
    data = {}
    name = ''

    if request.path == '/':

        data = new_tv_show.objects.annotate(total=F('criticScore') + F('audienceScore')).order_by('-total') # get objects by sums of criticScore and audienceScore in descending order.
        name = 'New TV Shows'

    elif request.path == '/best_tv_shows':
        
        data = best_tv_show.objects.all()
        name = 'Best TV Shows'

    elif request.path == '/new_movies':
        
        data = new_movie.objects.all()
        name = 'New Movies'

    elif request.path == '/best_recent_movies':

        data = best_movie.objects.annotate(total=F('criticScore') + F('audienceScore')).order_by('-total')
        name = 'Best Recent Movies'



    remain = len(data) % 5
    data = data[:len(data) - remain]
    
    
    if not data: # check if data is empty
        messages.error(request, 'Trouble loading database')
    


    return render(request, 'main.html', {'data': data,
                                         'name': name,
                                         'isAuthenticated': request.user.is_authenticated})



def executor(request):
    
    new_tv_show.objects.all().delete() # when updating db, delete all objects.

    base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/audience:upright~critics:fresh~sort:newest'

    data = main_parser(base_url, 3) # get data based on base_url and return it
    model = new_tv_show # assign the model reference to model variable

    create_instance(data, model) # pass the data and model reference to create_instance helper

    return HttpResponse('Updated {} database'.format(model.__name__))


def executor1(request):     
    
    best_tv_show.objects.all().delete() # when updating db, delete all objects.
    
    base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular'

    data = main_parser(base_url, 3) # get data based on base_url and return it
    model = best_tv_show # assign the model reference to model variable

    create_instance(data, model) # pass the data and model reference to create_instance helper

    return HttpResponse('Updated {} database'.format(model.__name__))


def executor2(request):


    new_movie.objects.all().delete() # when updating db, delete all objects.

    base_url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest' 


    data = main_parser(base_url, 3) # get data based on base_url and return it
    model = new_movie # assign the model reference to model variable

    create_instance(data, model) # pass the data and model reference to create_instance helper

    return HttpResponse('Updated {} database'.format(model.__name__))

    

def executor3(request):


    best_movie.objects.all().delete() # when updating db, delete all objects.

    base_url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:top_box_office' 

    data = main_parser(base_url, 3) # get data based on base_url and return it
    model = best_movie # assign the model reference to model variable

    create_instance(data, model) # pass the data and model reference to create_instance helper

    return HttpResponse('Updated {} database'.format(model.__name__))

    
def logout_view(request):
    logout(request)
    response = HttpResponse(status=200)
    response['HX-Redirect'] = '/'
    return response