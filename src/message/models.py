from django.db import models

# Create your models here.

class Message(models.Model):

    message = models.TextField(max_length=5000000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        splitted_message = self.message.split()
        return splitted_message[0]
    