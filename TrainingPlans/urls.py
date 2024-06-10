from django.urls import path
from TrainingPlans import views

urlpatterns = [
    path('trainingplans/', views.TrainingPlanListView.as_view()),
    path('trainingplans/<int:pk>/', views.TrainingPlanDetailView.as_view()),
]