from django.contrib import admin

from .models import new_tv_show, best_tv_show, new_movie

admin.site.register(new_tv_show)
admin.site.register(best_tv_show)
admin.site.register(new_movie)