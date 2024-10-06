from django.urls import path


from . import views


urlpatterns = [
    path('', views.main),
    path('best_tv_shows', views.main),
    path('new_movies', views.main),
    path('best_recent_movies', views.main),
    path('execute', views.executor),
    path('execute1', views.executor1),
    path('execute2', views.executor2),
    path('execute3', views.executor3)
]
