from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact_form.forms import ContactForm
from django.views.generic.base import TemplateView
from MotionPictures.settings import base
# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        Name=form.cleaned_data['first_name']
        Surname=form.cleaned_data['last_name']
        CHOICES = form.cleaned_data['CHOICES']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        subject= 'site contact form'
        from_email= base.EMAIL_HOST_USER
        to_email=[save_it.email,'ajaymundhe21@gmail.com'] 
        send_mail(subject,
                message, 
                from_email, 
                to_email,
                fail_silently=False)
    context = {
            "form":form,
    }
    return render(request, "contact.html",context)


