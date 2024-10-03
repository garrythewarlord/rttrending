from django.shortcuts import render, HttpResponse

from script import get_new_tv_shows, get_best_tv_shows, get_new_movies
from .models import new_tv_show, best_tv_show, new_movie

from django.db.models import F

# Create your views here.



def main(request):



    data = new_tv_show.objects.annotate(total=F('criticScore') + F('audienceScore')).order_by('-total') # get objects by sums of criticScore and audienceScore in descending order. 
    remain = len(data) % 5
    data = data[:len(data) - remain]

    return render(request, 'main.html', {'data': data})



def best(request):

    data = best_tv_show.objects.all()
    remain = len(data) % 5
    data = data[:len(data) - remain]


    return render(request, 'main.html', {'data': data})


def new_movies(request):

    data = new_movie.objects.all()
    remain = len(data) % 5
    data = data[:len(data) - remain]

    return render(request, 'main.html', {'data': data})

def executor(request):
    
    new_tv_show.objects.all().delete()

    # get current new tv shows
    data = get_new_tv_shows()

    #create instance
    for title in data:

        title = title
        image_src = data[title]['src_image']
        criticScore = data[title]['critics_score']
        audienceScore = data[title]['audience_score']
        last_episode_date = data[title]['last_episode_date']

        new_tv_show.objects.create(
            title=title,
            image_src=image_src,
            last_episode_date=last_episode_date,
            criticScore=criticScore,
            audienceScore=audienceScore,
        )


    return HttpResponse('Updated new tv show db!!')


def executor1(request):     
    
    best_tv_show.objects.all().delete()

    # get current new tv shows
    data = get_best_tv_shows()

    #create instance
    for title in data:
        
        title = title
        image_src = data[title]['src_image']
        criticScore = data[title]['critics_score']
        audienceScore = data[title]['audience_score']
        last_episode_date = data[title]['last_episode_date']


        best_tv_show.objects.create(
            title=title,
            image_src=image_src,
            last_episode_date=last_episode_date,
            criticScore=criticScore,
            audienceScore=audienceScore,
        )
    

    return HttpResponse('Updated best tv show db!')

def executor2(request):


    new_movie.objects.all().delete()

    data = get_new_movies()

    for title in data:

        title = title
        image_src = data[title]['src_image']
        criticScore = data[title]['critics_score']
        audienceScore = data[title]['audience_score']
        opening_date = data[title]['opening_date']

        new_movie.objects.create(
            title=title,
            image_src=image_src,
            opening_date=opening_date,
            criticScore=criticScore,
            audienceScore=audienceScore,
        )


    return HttpResponse('Updated new_movies_in_theaters db!')


