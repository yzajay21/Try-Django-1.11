from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact_form.forms import ContactForm
from django.template import Context
from django.views.generic.base import TemplateView
from django.template.loader import get_template
from MotionPictures.settings import production
from django.template.loader import render_to_string
# Create your views here.

def contact(request):
    form_class=ContactForm
    if request.method == 'POST':
        form=form_class(data=request.POST)
        if form.is_valid():
            first_name=request.POST.get('first_name','')
            last_name=request.POST.get('last_name','')
            CHOICES=request.POST.get('CHOICES','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            information =template.render(context)
            context =Context({
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'message':message,
                'CHOICES':CHOICES,
                })
            content=render_to_string(information,context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "24MotionPictures" +'',
                ['ajaymundhe21@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html',{
        'form':form_class,
        })






      #  subject= 'site contact form'
       # from_email= base.EMAIL_HOST_USER
        #to_email=[save_it.email,'ajaymundhe21@gmail.com'] 
        #send_mail(subject,
         #       message, 
          #      from_email, 
           #     to_email,
            #    fail_silently=False)



