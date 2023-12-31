import random

from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Question(models.Model):
    body = models.CharField(max_length=120)

    def __str__(self):
        return self.body


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'body'], name='unique_answers'),
        ]


class Game(models.Model):
    uuid = ShortUUIDField(length=8)
    questions = models.ManyToManyField(Question, through='GameQuestions')

    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        super(Game, self).save(*args, **kwargs)
        if not self.questions.exists():
            questions = list(Question.objects.all())
            random_questions = random.sample(questions, 10)
            order = 0
            for question in random_questions:
                game_question = GameQuestions(game=self, question=question, order=order)
                game_question.save()
                order += 1


class GameQuestions(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField()
    correct = models.BooleanField(null=True)

    def __str__(self):
        return 'Questions ' + str(self.order)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['game', 'question', 'order'], name='unique_order'),
        ]