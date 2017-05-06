# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Question
from .models import Choice

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		questions = Question.objects.all()
		return render(request, 'index.html', {'questions' : questions})

class PollPageView(TemplateView):
	template_name = "poll.html"
	def get(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		return render(request, 'poll.html', {'choice' : choice})

class ResultsPageView(TemplateView):
	template_name = "results.html"
	def get(self, request, **kwargs):
		id = request.GET.get("id")
		question = Question.objects.filter(id=id)
		choice = Choice.objects.filter(question_id=id)
		return render(request, 'results.html', {"question" : question})
