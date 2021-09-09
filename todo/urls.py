"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from tasks.views import (
    task_create_view,
    task_detail_view,
    task_search_view,
    task_delete_view,
    TaskUpdateView,
)

from .views import (
    index_view,
    )

from users.views import (
    login_view,
    logout_view,
    register,
)


urlpatterns = [
    path('home/', index_view, name='index'),
    # path('tasks/<int:id>/', task_detail_view),
    path('tasks/', task_search_view),
    path('tasks/create/', task_create_view, name='create'),
    path('delete/<int:id>/', task_delete_view, name="delete"),
    path('update/', index_view, name="detail"),
    path('update/<pk>/', TaskUpdateView.as_view()),
    re_path(r'tasks/(?P<id>\d+)/$', task_detail_view),
    path('register/', register, name="register"),
    path('', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
]

handler404 = 'tasks.views.handler404'
handler500 = 'tasks.views.handler500'