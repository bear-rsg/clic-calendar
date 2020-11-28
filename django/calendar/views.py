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

    Note that this is a more complex DetailView than normal, as it also includes:
        - A form for submitting a new answer to the current question
        - A list of answers related to the current question
    Therefore, suitable content needs to be added to this view's context, via the get_context_data() method
    """
    template_name = 'calendar/question-detail.html'
    queryset = models.Question.objects.filter(admin_published=True)

    def get_context_data(self, **kwargs):
        # Get current context
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        # Add form for creating an answer
        context['answer_create_form'] = forms.AnswerCreateForm
        # Add list of answers that relate to the current question and have been approved by admin
        context['answers'] = models.Answer.objects.filter(question=self.object.id, admin_approved=True)
        return context


class AnswerCreateView(CreateView):
    """
    Class-based view to create a new models.Answer object in the database
    This works by passing data to the forms.AnswerCreateForm form

    Note that this view doesn't have a template
    It's only intended to receive post requests and redirect if successful

    The template that includes the HTML form for submitting to this view is in the above QuestionDetailView.
    See the get_context_data() method in the QuestionDetailView for more details.
    """

    form_class = forms.AnswerCreateForm
    success_url = reverse_lazy('answer-create-success')


class AnswerCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the answer create success template
    """

    template_name = 'calendar/answer-create-success.html'
