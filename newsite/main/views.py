from email.message import EmailMessage
from multiprocessing import context

from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from .forms import ContactForm

# Create your views here.
def base(response):
    template = "base.html"

    return render(response, template, {})


def index(response):
    template = "index.html"

    return render(response, template, {})


def index_form(request):
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()        
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            
            
            send_mail(subject, message, email, ['karlosm961026@hotmail.com'])
            
            return HttpResponse("Correo enviado")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'success.html', context)

    """template = render_to_string('email.html',{
        'name': name,
        'phone': phone,
        'email': email,
        'message': message
    })

    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        ['karlosm961026@gmail.com']
    )

    send_mail(email)

    message_succes = messages.success(request, "Congratulations! " + name + " your message has been sent")
    return message_succes
    
    -----------------------------------------------------------------------------------------------------------

    template = render_to_string('index.html',{
                'name': name,
                'phone': phone,
                'email': email,
                'message': message
            })

    email = EmailMessage(
        subject,
        message,
        email,
        ['karlosm961026@hotmail.com',],
    )
    """
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return(request, 'index.html')
        
    form = ContactForm()
    context = {'form': form}
    return render(request, "Congratilations!!!!!!!!!", context)