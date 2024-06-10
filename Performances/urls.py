from django.urls import path
from Performances import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('events/<int:pk>/', views.EventListDetailView.as_view()),
    
]