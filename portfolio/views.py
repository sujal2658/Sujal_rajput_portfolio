from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            f'Message from {name}', 
            message, 
            email, 
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/portfolio/templates/index.html')
    return render(request, 'index.html')