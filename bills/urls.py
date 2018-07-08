from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.log_in, name='log_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.log_out, name='log_out'),
]
