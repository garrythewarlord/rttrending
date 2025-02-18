from django.db import models

# Create your models here.



class new_tv_show(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50)
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    

class best_tv_show(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50)
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    

class new_movie(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50) # opening_date
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    

class best_movie(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50) # opening_date
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class soon_in_theater(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50) # opening_date
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class popular_on_hbo(models.Model):
    
    title = models.CharField(max_length=100)
    image_src = models.URLField()
    last_episode_date = models.CharField(max_length=50) # opening_date
    criticScore = models.IntegerField() 
    audienceScore = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title