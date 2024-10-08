from django.urls import path


from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('best_tv_shows', views.main),
    path('new_movies', views.main),
    path('best_recent_movies', views.main),
    path('soon_in_theaters', views.main),
    path('popular_on_hbo', views.main),
    path('execute', views.executor),
    path('execute1', views.executor1),
    path('execute2', views.executor2),
    path('execute3', views.executor3),
    path('execute4', views.executor4),
    path('execute5', views.executor5),
    path('logout', views.logout_view)
]
