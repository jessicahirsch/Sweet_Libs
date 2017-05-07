# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django import forms

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
		vote_value = question.values('total_votes')[0]['total_votes']
		question.update(total_votes = vote_value+1)
		
		selected_choice = choice.filter(id=request.POST['choice'])
		voted_choice = selected_choice.values('votes')[0][u'votes']
		selected_choice.update(votes = voted_choice+1)

		return redirect('/results')






class ResultsPageView(TemplateView):
	template_name = "results.html"
	def get(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		return render(request, 'results.html', {"question" : question, "choice" : choice})

# class PollForm(forms.Form):
#     choice = forms.ChoiceField(required=False, widget=forms.RadioSelect)
