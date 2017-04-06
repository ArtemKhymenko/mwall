from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    #url(r'^home/$', views.home, name='home'),
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<pk>\d+)/add_comment_to_post/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^(?P<pk>\d+)/add_comment_to_comment/$', views.add_comment_to_comment, name='add_comment_to_comment'),



]
