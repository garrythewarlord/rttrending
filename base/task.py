from clery import shared_task
from models import new_tv_show

from script import get_new_tv_shows


@shared_task
def clear_and_update_database():

    new_tv_show.objects.all().delete() # delete all objects in the db


    data = get_new_tv_shows()

    for title in data:

        title = title
        image_src = data[title]['src_image']

        new_tv_show.objects.create(
            title=title,
            image_src=image_src
        )