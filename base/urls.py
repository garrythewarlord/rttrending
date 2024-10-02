from django.urls import path


from . import views


urlpatterns = [
    path('', views.main),
    path('best', views.best),
    path('execute', views.executor),
    path('execute1', views.executor1)

]


