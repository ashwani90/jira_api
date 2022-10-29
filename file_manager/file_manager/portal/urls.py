from django.urls import path

from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from .views.file import example_view, AboutView, FileListView,AsyncView

urlpatterns =  [
    # path('file/<int:id>/', views.year_archive),
    path('file/<int:id>', example_view, name="example"),
    path('about/', AboutView.as_view(), name="about"),
    path('files/', FileListView.as_view()),
    path('async/', AsyncView.as_view()),
]
