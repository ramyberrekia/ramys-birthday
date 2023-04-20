from django.urls import path
from .views import create_message

app_name = 'message'

urlpatterns = [
    path('create/', create_message, name='create_message'),
    # path('list/', list_messages, name='list_messages'),

    ]