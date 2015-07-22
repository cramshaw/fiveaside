from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Match, Team, UserProfile, Comment
from .forms import UserForm, UserProfileForm, CommentForm

import datetime

def home(request):
    context = RequestContext(request)
    return render_to_response('fives/home.html', {}, context)

def login_view(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fives/my_matches/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('fives/login.html', {}, context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/fives/')

def signup(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('fives/signup.html',
        {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'registered' : registered
        },
        context
        )

@login_required
def profile(request, user_id):
    context = RequestContext(request)
    return render_to_response('fives/profile.html', {
        'profile_id' : user_id
        }, context)

def all_matches_view(request):
    fixtures = Match.objects.filter(is_result=False).order_by('time')
    results = Match.objects.filter(is_result=True).order_by('-time')
    context = RequestContext(request,
        {'fixtures' : fixtures,
        'results' : results
        })
    return render_to_response('fives/all_matches.html', {}, context)

@login_required
def my_matches_view(request):
    user_team = UserProfile.objects.get(user=request.user.id).team_id
    fixtures = Match.objects.filter(Q(is_result=False),
        Q(home_team=user_team) | Q(away_team=user_team)).order_by('time')
    results = Match.objects.filter(Q(is_result=True),
        Q(home_team=user_team) | Q(away_team=user_team)).order_by('-time')
    context = RequestContext(request,
        {'fixtures' : fixtures,
        'results' : results
        })
    return render_to_response('fives/my_matches.html', {}, context)

def match_view(request, match_id):
    match_id = Match.objects.get(pk=match_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.match_id = match_id
            comment.time = datetime.datetime.now()
            comment.save()

        else:
            print form.errors

    else:
        comment_form = CommentForm()

    context = RequestContext(request, {
        'match_id' : match_id,
        'add_comment' : CommentForm(),
        })
    return render_to_response('fives/match.html', {}, context)

def team(request, team_id):
    #users and links to their profiles
    team = get_object_or_404(Team, pk=team_id)
    last_match = Team.get_last_match(team)
    next_match = Team.get_next_match(team)

    w, d, l = Team.get_WDL(team)
    context = RequestContext(request, {
        'team_id' : team,
        'w' : w,
        'd' : d,
        'l' : l,
        'last_match' : last_match,
        'next_match' : next_match,
        })
    return render_to_response('fives/team_page.html', {}, context)

def team_matches_view(request, team_id):
    team = Team.objects.get(pk=team_id)
    fixtures = Match.objects.filter(Q(is_result=False),
        Q(home_team=team_id) | Q(away_team=team_id)).order_by('time')
    results = Match.objects.filter(Q(is_result=True),
        Q(home_team=team_id) | Q(away_team=team_id)).order_by('-time')
    context = RequestContext(request,
        {'fixtures' : fixtures,
        'results' : results,
        'team' : team
        })
    return render_to_response('fives/team_matches.html', {}, context)