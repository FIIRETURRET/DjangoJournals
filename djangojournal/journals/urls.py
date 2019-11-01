from django.urls import path

from . import views

app_name = 'journals'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:journal_id>/', views.detail, name='detail'),
    path('new_journal/', views.new_journal, name='new_journal'),
]