from django.urls import path
from . import views

urlpatterns = [

    # Questions
    path('', views.QuestionListView.as_view(), name='question-list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),

    # Answers
    path('answer/', views.AnswerCreateView.as_view(), name='answer-create'),
    path('success/', views.AnswerCreateSuccessTemplateView.as_view(), name='answer-create-success'),

    # API
    path('api/', views.APITemplateView.as_view(), name='api'),
    path('api/questions', views.QuestionListAPIView.as_view(), name='api-question-list'),
    path('api/questions/<pk>/', views.QuestionRetrieveAPIView.as_view(),
         name='api-question-retrieve'),
    path('api/answers', views.AnswerListAPIView.as_view(), name='api-answer-list'),
    path('api/answers/<pk>/', views.AnswerRetrieveAPIView.as_view(), name='api-answer-retrieve')

]
