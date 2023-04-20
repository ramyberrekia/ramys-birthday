from django.urls import path
from .views import create_message, messages_list

app_name = 'message'

urlpatterns = [
    path('', create_message, name='create_message'),
    path('list/', messages_list, name='list_messages'),

    ]