from django.conf.urls import url
from app.views import log_in, log_out, sign_up, user_list, graph


urlpatterns = [
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^graph/$', graph, name='graph'),
    url(r'^$', user_list, name='user_list')
]