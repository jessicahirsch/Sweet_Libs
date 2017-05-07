# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Question, Choice
from .forms import PollForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		questions = Question.objects.all()
		return render(request, 'index.html', {'questions' : questions})

class PollPageView(TemplateView):

	def get(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		form = PollForm()
		return render(request, 'poll.html', {'choice' : choice, 'question': question, 'form': form})
	def post(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		# question.update(total_votes = question.total_votes+1)
		# voted_voice = choice.filter(id=request.POST['choice'])
		# voted_voice.update(votes = voted_voice.votes+1)
		return render(request, 'poll.html', {'response' : question.values('total_votes')})



    


class ResultsPageView(TemplateView):
    template_name = "results.html"
    def get(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		return render(request, 'results.html', {"question" : question})






# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))