from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)  # - заголовоквопроса
    text = models.TextField()  # - полный текст вопроса
    added_at = models.DateTimeField()  # - дата добавления вопроса
    rating = models.IntegerField()  # - рейтинг вопроса(число)
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)  # - автор вопроса
    likes = models.ManyToManyField(to=User)  # - список пользователей, поставивших "лайк"
    objects = QuestionManager()  # - extended Manager()

    class Meta:
        db_table = 'questions'


class Answer(models.Model):
    text = models.TextField()  # - текст ответа
    added_at = models.DateTimeField()  # - дата добавления ответа
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)  # - вопрос, к которому относится ответ
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)  # - автор ответа

    class Meta:
        db_table = 'answers'
