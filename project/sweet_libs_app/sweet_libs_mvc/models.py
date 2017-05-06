# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	name = models.CharField(max_length=200, default='Unnamed Question')
	question_text = models.TextField()
	total_votes = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name


class Choice(models.Model):
	name = models.CharField(max_length=200 ,default='Unnamed Choice')
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.name