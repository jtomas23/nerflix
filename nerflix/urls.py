from django.conf.urls import url
from nerflix import views
urlpatterns = [
    url(r'^list/$', views.movie_list, name='movie_list'),
    url(r'^new/$', views.movie_form, name='movie_create'),
    url(r'^edit/(?P<pk>\d+)$', views.movie_update, name='movie_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.movie_delete, name='movie_delete'),

]
