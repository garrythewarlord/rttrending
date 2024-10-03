from django.urls import path


from . import views


urlpatterns = [
    path('', views.main),
    path('best_tv_shows', views.best),
    path('new_movies', views.new_movies),
    path('execute', views.executor),
    path('execute1', views.executor1),
    path('execute2', views.executor2)
]
