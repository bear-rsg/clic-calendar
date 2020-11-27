from django.views.generic import (CreateView, TemplateView, ListView, DetailView)
from django.urls import reverse_lazy
from . import models
from . import forms


class QuestionListView(ListView):
    """
    Question: List
    Class-based view to show the question list template
    """

    template_name = 'calendar/question-list.html'
    queryset = models.Question.objects.filter(admin_published=True)


class QuestionDetailView(DetailView):
    """
    Question: Detail
    Class-based view to show the question detail template
    """

    template_name = 'calendar/question-detail.html'
    queryset = models.Question.objects.filter(admin_published=True)


class AnswerCreateView(CreateView):
    """
    Class-based view to show the answer create template
    """

    template_name = 'calendar/answer-create.html'
    form_class = forms.AnswerCreateForm
    success_url = reverse_lazy('answer-create-success')


class AnswerCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the answer create success template
    """

    template_name = 'calendar/answer-create-success.html'
