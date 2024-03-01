from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path('question/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/update/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('questions/list/', views.QuestionList.as_view(), name='question_list'),

    path('choice/create/', views.ChoiceCreateView.as_view(), name='choice_create'),
    path('choice/update/<int:pk>/', views.ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', views.ChoiceDeleteView.as_view(), name='choice_delete'),
]



""" urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
] """

""" app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
 """