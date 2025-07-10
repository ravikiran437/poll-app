from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project/", views.project, name="project"),
    path("question/<int:question_id>/",views.question_view, name="question_detail"),
    path("results/", views.results, name="results"),
]
