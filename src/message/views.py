from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MessageCreateForm
from .models import Message

def create_message(request):
    form = MessageCreateForm()
    if request.method == 'POST':
        form = MessageCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, message='c reglé Ramy rw l79o l msg dylk, nchlh yaerf shkoun li beato')
    return render(request, 'create.html', {'form':form})

def messages_list(request):
    if request.user.is_staff:
        messages = Message.objects.all()
        return render(request, 'list.html', {'bd_messages':messages})
    else:
        return redirect('message:create_message')