from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^all_matches/$', views.all_matches_view, name='all_matches'),
    url(r'^my_matches/$', views.my_matches_view, name='my_matches'),
    #needs a league model adding to expand to more leagues
    url(r'^match/(?P<match_id>[0-9]+)/$', views.match_view, name='match'),
    url(r'^team/(?P<team_id>[0-9]+)/$', views.team, name='team'),
    url(r'^team_matches/(?P<team_id>[0-9]+)/$', views.team_matches_view, name='team_matches'),
]