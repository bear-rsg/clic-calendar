from django.views.generic import (CreateView, TemplateView, ListView, DetailView)
from rest_framework.generics import (RetrieveAPIView, ListAPIView)
from django.urls import reverse_lazy
from . import (models, forms, serializers)


class QuestionListView(ListView):
    """
    Question: List
    Class-based view to show the question list template
    """

    template_name = 'researchdata/question-list.html'
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
    template_name = 'researchdata/question-detail.html'
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

    template_name = 'researchdata/answer-create-success.html'


# API views


class APITemplateView(TemplateView):
    """
    Display the API template
    """
    template_name = 'researchdata/api.html'


class QuestionListAPIView(ListAPIView):
    """
    Return list of all questions
    """
    queryset = models.Question.objects.filter(admin_published=True)
    serializer_class = serializers.QuestionSerializer


class QuestionRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific question
    """
    queryset = models.Question.objects.filter(admin_published=True)
    serializer_class = serializers.QuestionSerializer


class AnswerListAPIView(ListAPIView):
    """
    Return list of all answers
    """
    queryset = models.Answer.objects.filter(admin_approved=True)
    serializer_class = serializers.AnswerSerializer


class AnswerRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific answer
    """
    queryset = models.Answer.objects.filter(admin_approved=True)
    serializer_class = serializers.AnswerSerializer
