from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer
from django.template import loader

# Create your views here.

# Main view or rather home view
def index(request):
    latest_question_list = Question.objects.order_by("-q_date")[:5]
    template = loader.get_template('learn/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    
    return render(request, 'learn/index.html', context)



def questions(request, question_id):
    return HttpResponse("This is question %s" %question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'learn/results.html', {'question': question})
  

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected = question.answer_set.get(pk=request.POST['choice'])
    except (KeyError, Answer.DoesNotExist):
         return render(
             request,
             'learn/details.html',
             {
                 'question': question,
                 
                 'error_message': 'You did not select an option'
             },
         )
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse("learn:results", args=(question.id,))) 
        # return HttpResponse('You are voting on question %s' % question_id) 


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Does Not Exist')
    # answer = get_object_or_404(Answer, pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'learn/details.html', {'question':question})

def blank(request):
    context = {
        'field': 'backend',
        'framework': 'Django'
    }
    
    return render(request, 'learn/blank.html', context)