from celery import shared_task

from .helpers import create_instance
from script import main_parser

from .models import new_tv_show, best_tv_show, new_movie, best_movie, soon_in_theater, popular_on_hbo


@shared_task
def my_scheduled_task():

    # updating databases

    try:
        new_tv_show.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/audience:upright~critics:fresh~sort:newest'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = new_tv_show # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        best_tv_show.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = best_tv_show # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        new_movie.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = new_movie # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        best_movie.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:top_box_office'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = best_movie # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        soon_in_theater.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/movies_coming_soon/'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = soon_in_theater # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        popular_on_hbo.objects.all().delete() # when updating db, delete all objects.
        base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:max~sort:popular'
        data = main_parser(base_url, 3) # get data based on base_url and return it
        model = popular_on_hbo # assign the model reference to model variable
        create_instance(data, model) # pass the data and model reference to create_instance helper

        print("Task run successfully.")
        
    except:
        print("Run into an error.")
    
    return None