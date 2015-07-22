from django.contrib import admin
import models

class MatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'home_team', 'away_team', 'time', 'is_result']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'match_id', 'user']
    raw_id_fields = ['user', 'match_id']

admin.site.register(models.UserProfile)
admin.site.register(models.Team)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Match, MatchAdmin)