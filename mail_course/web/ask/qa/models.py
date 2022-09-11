from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(to=User, related_name='question_likes')
    objects = QuestionManager()

    # class Meta:
    #     db_table = 'questions'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)

    # class Meta:
    #     db_table = 'answers'
# Failed test #4. Failed to create question model, check db connection