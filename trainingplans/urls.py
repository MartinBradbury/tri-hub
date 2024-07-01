from django.urls import path
from trainingplans import views

urlpatterns = [
    path('trainingplans/', views.TrainingPlanListView.as_view()),
    path('trainingplans/<int:pk>/', views.TrainingPlanDetailView.as_view()),
]
