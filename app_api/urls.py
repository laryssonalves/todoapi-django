from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

api_patterns = [
    path('', views.ApiOverview.as_view(), name='ApiOveriew'),
    path('tasks/', views.TaskList.as_view(), name='TaskList'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='TaskDetail'),
]

api_patterns = format_suffix_patterns(api_patterns)