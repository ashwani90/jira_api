from django.urls import path

from . import views
from .views.project import ProjectView 
from .views.task import TaskView 
from .views.module import ModuleView 
from .views.user import UserView
from .views.user import login_user

from portal.views.module import ModuleView
from rest_framework.routers import DefaultRouter


urlpatterns =  [
    path('module/', ModuleView.as_view(), name="modules"),
    path('project/', ProjectView.as_view(), name="modules"),
    path('task/', TaskView.as_view(), name="task"),
    path('user/', UserView.as_view(), name="user"),
    path('login/', login_user, name="login"),
]