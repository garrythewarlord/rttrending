
from bs4 import BeautifulSoup
import requests

import os
from dotenv import load_dotenv
load_dotenv()




# helpers
def clean_score(score):
    cleaned = score.replace(' ', '').replace('%', '')
    return int(float(cleaned)) if cleaned.isdigit() else 0


def get_new_tv_shows(page=3):

    base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/audience:upright~critics:fresh~sort:newest' 

    if page: # checks if page exists
        base_url += '?page={}'.format(page) # adds pages to query through

    html = requests.get(base_url) # gets content
    soup = BeautifulSoup(html.content, 'html.parser') # parses content
    titles = soup.find_all('div', class_='flex-container') # main title body
    trending_tv_titles = {} # empty dict




    for tv in titles: # iterate through titles
        tv_name = tv.find('span', class_='p--small').text.replace('\n', '').strip() # get title name

        scores = tv.find_all('rt-text')
        
        criticsScore = clean_score(scores[0].text)
        audienceScore = clean_score(scores[-1].text)

        

    
        trending_tv_titles[tv_name] = {
            'src_image': tv.find('rt-img').get('src'), # parse source image url
            'last_episode_date': tv.find('span', class_='smaller').text.replace('\n', '').strip(), # parse last episode date
            'critics_score': criticsScore,
            'audience_score': audienceScore
        }

    
    return trending_tv_titles # return titles



def get_best_tv_shows(page=3):

    base_url = 'https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular' 

    if page: # checks if page exists
        base_url += '?page={}'.format(page) # adds pages to query through

    html = requests.get(base_url) # gets content
    soup = BeautifulSoup(html.content, 'html.parser') # parses content
    titles = soup.find_all('div', class_='flex-container') # main title body
    best_tv_titles = {} # empty dict




    for tv in titles: # iterate through titles
        tv_name = tv.find('span', class_='p--small').text.replace('\n', '').strip() # get title name

        scores = tv.find_all('rt-text')
        
        criticsScore = clean_score(scores[0].text)
        audienceScore = clean_score(scores[-1].text)

        
        best_tv_titles[tv_name] = {
            'src_image': tv.find('rt-img').get('src'), # parse source image url
            'critics_score': criticsScore,
            'audience_score': audienceScore
        }

    
    return best_tv_titles # return titles



print(get_best_tv_shows())


# def get_imdb_link(title='Reasonable Doubt'):

#     api_key = os.getenv('api_key')

#     response = requests.get("https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(api_key, title)).json()
    
#     if response['results']:
#         object = response['results'][0]
#         popularity_rating = object['popularity']
#         return popularity_rating




# print(get_imdb_link())
# # print(get_new_tv_shows())

