from django.shortcuts import render
from polls.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from polls.forms import QuestionModelForm
from django.utils import timezone


# Create your views here.
def view_allquestions(request):
    questions = Question.objects.all()
    p = Paginator(Question.objects.all(), 1)
    page = request.GET.get('page')
    question = p.get_page(page)

    context = {
        "questions": questions,
        "question": question,

    }
    return render(request, "polls/allquestions.html", context)


def view_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/question.html", context)


def create(request):
    if request.method == "GET":
        form = QuestionModelForm()
        context = {
            "form": form
        }
        return render(request, "polls/create.html", context)
    elif request.method == "POST":

        form = QuestionModelForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.pub_date = timezone.now()
            new_question.save()
            return redirect("/polls")


def delete(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect("/polls")
