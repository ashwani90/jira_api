from django.urls import path

from . import views
from .views.project import ProjectView as Project
from .views.task import TaskView as Task
from .views.module import ModuleView as Module

urlpatterns = [
    path('project/', Project.as_view(), name='project'),
    path('task/', Task.as_view(), name='task'),
    path('module/', Module.as_view(), name='module'),
]
