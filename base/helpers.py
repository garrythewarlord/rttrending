


def create_instance(data, model):
    #create instance
    for title in data:

        title = title
        image_src = data[title]['src_image']
        criticScore = data[title]['critics_score']
        audienceScore = data[title]['audience_score']
        last_episode_date = data[title]['last_episode_date']

        model.objects.create(
            title=title,
            image_src=image_src,
            last_episode_date=last_episode_date,
            criticScore=criticScore,
            audienceScore=audienceScore,
        )
    
    return 'Success!'




