from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/addtopic/', views.AddTopic.as_view(), name='addtopic'),
    path('topics/delete/<int:topic_id>', views.deltopic, name='deltopic'),
    path('topics/<int:topic_id>/edittopic/', views.edittopic, name='edittopic'),
    path('topics/<int:topic_id>/addentry/', views.AddEntry.as_view(), name='addentry'),
]
