from django.urls import path

from . import views
from .views.project import ProjectView 
from .views.task import TaskView 
from .views.module import ModuleView 
from .views.user import UserView
from .views.user import login_user,register

from portal.views.module import ModuleView
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

handler404 = 'mysite.views.my_custom_page_not_found_view'
handler500 = 'mysite.views.my_custom_error_view'
handler403 = 'mysite.views.my_custom_permission_denied_view'
handler400 = 'mysite.views.my_custom_bad_request_view'

urlpatterns =  [
    path('module/', ModuleView.as_view(), name="modules"),
    path('project/', ProjectView.as_view(), name="modules"),
    path('task/', TaskView.as_view(), name="task"),
    path('user/', UserView.as_view(), name="user"),
    path('login/', login_user, name="login"),
    path('register/', register, name="register"),
]