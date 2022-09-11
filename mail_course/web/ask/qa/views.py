from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.urls import reverse
from models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    questions = Question.objects.new()
    try:
        limit = int(request.GET.get('limit', 10))
        if limit > 100:
            limit = 10
    except ValueError:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    }
    return render(request=request, template_name='main.html', context=context)


def popular(request):
    questions = Question.objects.popular()
    try:
        limit = int(request.GET.get('limit', 10))
        if limit > 100:
            limit = 10
    except ValueError:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    }
    return render(request=request, template_name='popular.html', context=context)


def question(request, question_id: int):
    try:
        quest = Question.objects.get(pk=question_id)[0]
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=quest)
    except Answer.DoesNotExist:
        answers = None
    context = {
        'question': quest,
        'answers': answers,
    }
    return render(request=request, template_name='question.html', context=context)

