from django.urls import path
from . import views

urlpatterns = [
    # Questions
    path('', views.QuestionListView.as_view(), name='question-list'),
    path('<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    # Answers
    path('<int:pk>', views.AnswerDetailView.as_view(), name='answer-detail'),
    path('answer/', views.AnswerCreateView.as_view(), name='answer-create'),
    path('success/', views.AnswerCreateSuccessTemplateView.as_view(), name='answer-create-success'),
]
