from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Question, Answer
from .forms import AskForm, AnswerForm


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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_to = '/question/' + str(question_id)
            return HttpResponseRedirect(redirect_to=redirect_to)
    try:
        quest = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=quest)
    except Answer.DoesNotExist:
        answers = None
    context = {
        'question': quest,
        'answers': answers,
        'form': AnswerForm(),
    }
    return render(request=request, template_name='question.html', context=context)


def ask(request):
    if request.method == 'GET':
        form = AskForm()
    elif request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save()
            redirect_to = '/question/' + str(quest.id)
            return HttpResponseRedirect(redirect_to=redirect_to)
    else:
        raise HttpResponseForbidden
    context = {'form': form}
    return render(request=request, template_name='ask.html', context=context)


def signup(request):
    ...


def login(request):
    ...
