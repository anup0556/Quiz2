"""
URL configuration for quizapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from answers.views import SubmitAnswerView
from leaderboard.views import LeaderboardView
from questions.views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('api/questions/', QuestionListView.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),  # Add this line
]
