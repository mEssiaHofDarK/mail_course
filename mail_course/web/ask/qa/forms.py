import datetime

from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    _user = User()

    # def clean(self):
    #     ...

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data.get('question')
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
        # if not question:
            raise forms.ValidationError('not found question')
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

    def save(self):
        self.cleaned_data['last_login'] = datetime.datetime.now()
        user = User.objects.create_user(**self.cleaned_data)
        resp = user.save()
        return resp


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

