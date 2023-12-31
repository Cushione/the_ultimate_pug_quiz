from django.shortcuts import render, redirect
from django.views import View

from quiz.forms import QuizForm
from quiz.models import Game, Answer
import random


class HomeView(View):

    @staticmethod
    def get(request):
        existing = Game.objects.filter(session=request.session.session_key, finished=False).first()
        return render(request, 'home.html', {'existing': existing})


def start_new_game(request):
    existing = Game.objects.filter(session=request.session.session_key, finished=False).first()
    if existing:
        existing.finished = True
        existing.save()
    new_game = Game.objects.create(session_id=request.session.session_key)
    return redirect('quiz:game', new_game.uuid)


class GameView(View):
    @staticmethod
    def get(request, game_uuid):
        game = Game.objects.filter(uuid=game_uuid).first()
        if game is None:
            return redirect('quiz:home')
        else:
            questions = sorted(list(game.gamequestions_set.all()), key=lambda x: x.order)
            try:
                next_question = next(question for question in questions if question.correct is None)
                return render(request, 'quiz.html', {'game': game, 'game_question': next_question})
            except StopIteration:
                game.finished = True
                game.save()
                return redirect('quiz:result', game_uuid=game_uuid)

    @staticmethod
    def post(request, game_uuid):
        game = Game.objects.get(uuid=game_uuid)
        if game is None:
            return redirect('quiz:home')
        else:
            form = QuizForm(request.POST)
            if form.is_valid():
                answer_id = form.cleaned_data["answer"]
                answer = Answer.objects.get(id=answer_id)
                question_id = answer.question.id
                game_question = game.gamequestions_set.get(question_id=question_id)
                if game_question.correct is None:
                    game_question.correct = answer.right
                    game_question.save()
                    return render(request, 'quiz.html',
                                  {'game': game, 'game_question': game_question, 'answer_id': answer_id})
            return redirect('quiz:game', game_uuid=game_uuid)


class ResultView(View):
    @staticmethod
    def get(request, game_uuid):
        game = Game.objects.get(uuid=game_uuid)
        return render(request, 'result.html', {'score': game.score_percent})
