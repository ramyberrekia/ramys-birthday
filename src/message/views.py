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
            messages.add_message(request,messages.SUCCESS, message='C bon l msg dylk raho teb3t l Ramy, nchlh yaerf shkoun li beato')
    return render(request, 'create.html', {'form':form})
