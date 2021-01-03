from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import Contacts
from .models import Contact


class ContactView(ListView):
    model = Contact()
    template_name = 'contacts.html'
    context_object_name = 'con'

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact_db = Contact(surname = name, last_name = last_name, phone = phone, email = email)
        contact_db.save()
        return render(request, "index.html", {'name': name, 'last_name': last_name, 'phone': phone, 'email': email,})
    else:
        contact = Contacts
        return render(request, "index.html", {'form': contact})

