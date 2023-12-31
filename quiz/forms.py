from django import forms


class QuizForm(forms.Form):
    answer = forms.IntegerField()
