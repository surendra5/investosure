# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import internform
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
# Create your views here.
def index(request):
    context = {}
    return render(request,'home/home.html', context)

def about(request):
    context = {}
    return render(request,'home/about.html', context)

def internprog(request):
    context = {}
    return render(request,'home/internprog.html', context)

def finance(request):
    context = {}
    return render(request,'home/finance.html', context)

def trading(request):
    context = {}
    return render(request,'home/trading.html', context)
def rpo(request):
    context = {}
    return render(request,'home/rpo.html', context)

def training(request):
    context = {}
    return render(request,'home/training.html', context)

def location(request):
    context = {}
    return render(request,'home/location.html', context)

def whatwedo(request):
    context = {}
    return render(request,'home/about.html', context)

def internapply(request):
    if request.method == 'POST':
        #to pull last filled details
        form = internform(request.POST)
        #cleaned form after submit
        #form = GymkhanaForm()
        if form.is_valid():
            form.save()
            form = internform()
    else:
        form = internform()
    context_data = {'form': form}
    return render(request, 'home/internform.html', context_data)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['surendrameena5@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context_data = {'form': form}
    return render(request, 'home/contact.html', context_data)

def success(request):
    return HttpResponse('Success! Thank you for your message.')
