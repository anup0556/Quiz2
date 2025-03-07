from django.contrib import admin
from django.urls import path
from answers.views import SubmitAnswerView
from leaderboard.views import LeaderboardView  # Make sure it's LeaderboardView, not LeaderBoardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]