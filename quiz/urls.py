from django.urls import path, include
import quiz.views as views

app_name = 'quiz'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('game/new', views.start_new_game, name='new_game'),
    path('game/<str:game_uuid>', views.GameView.as_view(), name='game'),
]
