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
    model = models.Question.objects.filter(admin_published=True)


class QuestionDetailView(DetailView):
    """
    Question: Detail
    Class-based view to show the question detail template
    """

    template_name = 'calendar/question-detail.html'
    model = models.Question.objects.filter(admin_published=True)


class AnswerListView(ListView):
    """
    Answer: List
    Class-based view to show the answer list template
    """

    template_name = 'calendar/answer-list.html'
    model = models.Answer.objects.filter(admin_approved=True)
    paginate_by = 50


class AnswerDetailView(DetailView):
    """
    Answer: Detail
    Class-based view to show the answer detail template
    """

    template_name = 'calendar/answer-detail.html'
    model = models.Answer.objects.filter(admin_approved=True)


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
