from multiprocessing import context
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import contacto_info


# Create your views here.
def base(response):
    template = "base.html"

    return render(response, template, {})


def index(response):
    template = "index.html"

    return render(response, template, {})


def my_list(response):
    ls = contacto_info.objects.get(id=2)
    template = "list.html"

    return render(response, template, {"ls":ls})

    
def contact(response):
    template = "contact.html"

    if response.method == "POST":
        forms = ContactForm(response.POST)

        if forms.is_valid():
            forms.save()
    else:
        forms = ContactForm()
    
    context = {
        'form': forms,
    }

    return render(response, template, context)

def project_views(response):
    return HttpResponse("<h1> You are looking for the new project </h1>")