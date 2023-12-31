from django.urls import path, include
import quiz.views as views

app_name = 'quiz'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
