from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=20)

    def get_WDL(team_id):
        w = 0
        d= 0
        l = 0
        matches = Match.objects.filter(
            Q(home_team=team_id) | Q(away_team=team_id),
            Q(is_result=True)
        )
        for match in matches:
            winner = Match.winner(match)
            if winner == 'D':
                d += 1
            elif winner == team_id:
                w +=1
            else:
                l += 1
        return w, d, l 

    def H2H(team_1, team_2):
        team1 = 0
        team2 = 0
        draw = 0
        matches = Match.objects.filter(
            Q(home_team=team_1, away_team=team_2) | Q(home_team=team_2, away_team=team_1),
            Q(is_result=True)
        )
        for match in matches:
            winner = Match.winner(match)
            if winner == "D":
                draw +=1
            elif winner == team_1:
                team1 +=1
            elif winner == team_2:
                team2 += 1
        return team1, team2, draw


    def get_last_match(team_id):
        try:
            match = Match.objects.filter(
                Q(is_result=True),
                Q(home_team=team_id) | Q(away_team=team_id)).latest()
            return match
        except:
            return "No previous matches"

    def get_next_match(team_id):
        try:
            match = Match.objects.filter(
                Q(is_result=False),
                Q(home_team=team_id) | Q(away_team=team_id)).earliest()
            return match
        except:
            return "No scheduled matches"
   

    def __str__(self):
        return self.name


class Match(models.Model):
    time = models.DateTimeField('time')
    home_team = models.ForeignKey('Team', related_name = 'home')
    away_team = models.ForeignKey('Team', related_name = 'away')
    home_goals = models.IntegerField(null=True, blank=True)
    away_goals = models.IntegerField(null=True, blank=True)
    match_details = models.TextField(max_length=500, blank=True)
    is_result = models.BooleanField(default=False)

    class Meta: 
        get_latest_by = 'time'

    def winner(self):
        #could make this ignore instances of self.home_goals == None
        if self.home_goals == self.away_goals:
            return "D"
        elif self.home_goals > self.away_goals:
            return self.home_team
        elif self.away_goals > self.home_goals:
            return self.away_team

    def __str__(self):
        if self.home_goals:
            return '%s %d v %d %s' % (self.home_team, self.home_goals, self.away_goals, self.away_team)
        else:
            return '%s v %s' % (self.home_team, self.away_team)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    team = models.ForeignKey('Team', null=True, related_name = 'player')

    def __str__(self):
        return self.user.username



class Comment(models.Model):
    match_id = models.ForeignKey('Match', related_name='comment')
    user = models.ForeignKey(User)
    comment = models.TextField(max_length=200)
    time = models.DateTimeField('time')
    def __str__(self):
        return self.comment



