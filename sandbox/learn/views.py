from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-q_date")[:5]
    template = loader.get_template('learn/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'learn/index.html', context)
    # return HttpResponse(template.render(context, request))


def questions(request, question_id):
    return HttpResponse("This is question %s" %question_id)

def results(request, question_id):
    response = 'This is the result for No.%s'
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse('You are voting on question %s' % question_id) 

def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Does Not Exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'learn/details.html', {'question':question})

def blank(request):
    return render(request, 'learn/blank.html')