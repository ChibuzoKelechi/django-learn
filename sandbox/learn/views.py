from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Answer
from django.template import loader

# Create your views here.

# Main view or rather home view
class IndexView(generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('q_date')[:5]

# Other Generic views
class DetailView(generic.DetailView):
    model = Question
    template_name='learn/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'learn/results.html'
  

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
    
# Blank/Static page 
def blank(request):
    context = {
        'field': 'backend',
        'framework': 'Django'
    }
    
    return render(request, 'learn/blank.html', context)