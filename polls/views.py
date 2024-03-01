from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

class QuestionCreateView(CreateView):
    model = Question
    fields = ['pub_date', 'question_text']
    template_name = 'polls/question_form.html'  
    success_url = reverse_lazy('polls:index')  
    def get_initial(self):
        initial = super().get_initial()
        initial['pub_date'] = timezone.now()  
        return initial

class QuestionUpdateView( PermissionRequiredMixin ,UpdateView):
    model = Question 
    fields = ['pub_date','question_text']
    template_name = 'polls/question_update.html'  
    success_url = reverse_lazy('polls:question_list') 
    permission_required = 'polls.change_question'

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/question_delete.html'  
    success_url = reverse_lazy('polls:index')  

class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'polls/choice_form.html' 
    success_url = reverse_lazy('polls:index')  

class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ['choice_text']
    template_name = 'polls/choice_update.html'  
    success_url = reverse_lazy('polls:question_list')  

class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'polls/choice_delete.html'  
    success_url = reverse_lazy('polls:index')

class QuestionList(ListView):
    model = Question
    template_name = 'polls/list.html'
    




""" ----------------------------------------------------------------------------------------------------------------------------------------------------- """

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions.""" """  return Question.objects.order_by("-pub_date")[:5] """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())   
    def get(self, request, *args, **kwargs):
        print("Rendering template:", self.template_name)
        return super().get(request, *args, **kwargs)




""" 
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
 """

""" def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question}) """

""" def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question}) """
""" 
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
 """
""" 
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) """


""" 
def results(request, question_id):
    # Retrieve the question object or raise a 404 error if it doesn't exist
    question = get_object_or_404(Question, pk=question_id)
    
    # Calculate the results
    total_votes = 0
    results = {}
    for choice in question.choice_set.all():
        total_votes += choice.votes
        results[choice.choice_text] = choice.votes
    
    # Render the results template with the question object and results
    return render(request, 'polls/results.html', {'question': question, 'results': results, 'total_votes': total_votes})

 """


""" 
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id) """

""" def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output) """
""" 
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context) """


