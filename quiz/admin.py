from django.contrib import admin
from django.forms import BaseInlineFormSet, forms

import quiz.models as models


class AnswerAdminInlineFormset(BaseInlineFormSet):

    def clean(self):
        super().clean()
        valid = False
        for form in self.forms:
            try:
                if form.cleaned_data and form.cleaned_data['right'] is not None:
                    if form.cleaned_data['right']:
                        valid = True
                        break

            except AttributeError:
                pass
        if not valid:
            raise forms.ValidationError('You must have at least one correct answer')


class AnswerAdminInline(admin.TabularInline):
    model = models.Answer
    formset = AnswerAdminInlineFormset


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdminInline]


class GameQuestionsAdminInline(admin.TabularInline):
    model = models.GameQuestions
    exclude = ('order',)
    readonly_fields = ('question', 'correct')
    can_delete = False
    max_num = 10


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    model = models.Game

    list_display = ('uuid', 'session', 'score')

    inlines = [GameQuestionsAdminInline]
    readonly_fields = ['session']
    exclude = ('questions', 'uuid')

    def has_add_permission(self, request, obj=None):
        return False
