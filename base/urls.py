from django.urls import path
from . import views
from .views import TaskList, TaskDetail, DeleteView, CustomLoginView, RegisterPage , CreateTask, UpdateTask #, TaskCreate , TaskUpdate
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<uuid:pk>/', TaskDetail.as_view(), name='task'),
    # path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-create', views.CreateTask, name='task-create'),
    # path('task-update/<uuid:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-update/<uuid:pk>/', views.UpdateTask, name='task-update'),
    path('task-delete/<uuid:pk>/', DeleteView.as_view(), name='task-delete'),
]