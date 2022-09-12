from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     ...

    def save(self):
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
