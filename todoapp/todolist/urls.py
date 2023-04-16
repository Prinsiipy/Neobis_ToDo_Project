from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit'),
    path('add_todo/<int:todo_id>/', views.add_todo, name='add_todo'),
]
