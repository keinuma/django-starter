# url関数のimport
from django.conf.urls import url

from . import views


# ルーティングの設定
urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),

    url(r'^header/$', views.header, name='header'),

    url(r'^get$', views.get_requester, name='get'),

    url(r'^post$', views.post_requester, name='post'),

    url(r'^response/$', views.response_getter, name='response'),

    url(r'^pages/(?P<id>\d+)/$', views.pages, name='pages'),

    url(r'^news/(?P<slug>[-\w]+)/$', views.news, name='news'),
]
