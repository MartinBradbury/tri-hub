from django.urls import path
from performances import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('events/<int:pk>/', views.EventListDetailView.as_view()),
    path('performances/', views.PerformanceListView.as_view()),
    path('performances/<int:pk>/', views.PerformanceDetailView.as_view()),
]
