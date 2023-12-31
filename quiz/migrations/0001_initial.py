# Generated by Django 5.0 on 2023-12-30 07:50

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=8, max_length=8, prefix='')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='GameQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('correct', models.BooleanField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.game')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='questions',
            field=models.ManyToManyField(through='quiz.GameQuestions', to='quiz.question'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=120)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.AddConstraint(
            model_name='gamequestions',
            constraint=models.UniqueConstraint(fields=('game', 'question', 'order'), name='unique_order'),
        ),
        migrations.AddConstraint(
            model_name='answer',
            constraint=models.UniqueConstraint(fields=('question', 'body'), name='unique_answers'),
        ),
    ]