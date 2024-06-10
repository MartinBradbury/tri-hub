from django.urls import path
from Performances import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    
]