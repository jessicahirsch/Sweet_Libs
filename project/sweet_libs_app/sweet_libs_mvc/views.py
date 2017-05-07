# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django import forms

from .models import Question, Choice
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
		return render(request, 'poll.html', {'choice' : choice, 'question': question})
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
		return render(request, 'results.html', {"question" : question, "choice" : choice})

# class PollForm(forms.Form):
#     choice = forms.ChoiceField(required=False, widget=forms.RadioSelect)
