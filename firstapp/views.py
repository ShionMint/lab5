from django.shortcuts import render

from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Owner, Object, Event, Popularity, Users
from .forms import DataOwner, DataObject, DataEvent, DataPopularity, DataUsers

# Create your views here.

def logout(request):
    return render(request, "registration/login.html")

def index(request):
    return render(request, "index.html")

def index_owner(request):
    index_form = DataOwner()
    index_data = Owner.objects.all()
    return render(request, "firstapp/Template_owner.html", {"form": index_form, "data": index_data})

class view_owner(View):
    def add_owner(request):
        if request.method == "POST":
            add_data = Owner()
            add_data.type_owner = request.POST.get("type_owner")
            add_data.name_owner = request.POST.get("name_owner")
            add_data.full_name = request.POST.get("full_name")
            add_data.contact_number = request.POST.get("contact_number")
            add_data.opening_date = request.POST.get("opening_date")
            add_data.save()
            return HttpResponseRedirect("/home/owner")

    def del_owner(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Owner.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/owner")

    def update_owner(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Owner.objects.get(id=update_int)
            update_data.type_owner = request.POST.get("type_owner")
            update_data.name_owner = request.POST.get("name_owner")
            update_data.full_name = request.POST.get("full_name")
            update_data.contact_number = request.POST.get("contact_number")
            update_data.opening_date = request.POST.get("opening_date")
            update_data.save()
            return HttpResponseRedirect("/home/owner")

def index_object(request):
    index_form = DataObject()
    index_data = Object.objects.all()
    return render(request, "firstapp/Template_object.html", {"form": index_form, "data": index_data})

class view_oblect(View):
    def add_object(request):
        if request.method == "POST":
            add_data = Object()
            add_data.owner_id = Owner.objects.get(id=request.POST.get("owner_id"))
            add_data.name = request.POST.get("name")
            add_data.type = request.POST.get("type")
            add_data.address = request.POST.get("address")
            add_data.number_of_seats = request.POST.get("number_of_seats")
            add_data.save()
            return HttpResponseRedirect("/home/object")

    def del_object(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Object.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/object")

    def update_object(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Object.objects.get(id=update_int)
            update_data.owner_id = Object.objects.get(id=request.POST.get("owner_id"))
            update_data.name = request.POST.get("name")
            update_data.type = request.POST.get("type")
            update_data.address = request.POST.get("address")
            update_data.number_of_seats = request.POST.get("number_of_seats")
            update_data.save()
            return HttpResponseRedirect("/home/object")

def index_event(request):
    index_form = DataEvent()
    index_data = Event.objects.all()
    return render(request, "firstapp/Template_event.html", {"form": index_form, "data": index_data})

class view_event(View):
    def add_event(request):
        if request.method == "POST":
            add_data = Event()
            add_data.object_id = Object.objects.get(id=request.POST.get("object_id"))
            add_data.date_of_event = request.POST.get("date_of_event")
            add_data.type_of_event = request.POST.get("type_of_event")
            add_data.save()
            return HttpResponseRedirect("/home/event")

    def del_event(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Event.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/event")

    def update_event(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Event.objects.get(id=update_int)
            update_data.object_id = Event.objects.get(id=request.POST.get("object_id"))
            update_data.date_of_event = request.POST.get("date_of_event")
            update_data.type_of_event = request.POST.get("type_of_event")
            update_data.save()
            return HttpResponseRedirect("/home/event")

def index_popularity(request):
    index_form = DataPopularity()
    index_data = Popularity.objects.all()
    return render(request, "firstapp/Template_popularity.html", {"form": index_form, "data": index_data})

class view_popularity(View):
    def add_popularity(request):
        if request.method == "POST":
            add_data = Popularity()
            add_data.object_id = Object.objects.get(id=request.POST.get("object_id"))
            add_data.date = request.POST.get("date")
            add_data.number_of_visitors = request.POST.get("number_of_visitors")
            add_data.save()
            return HttpResponseRedirect("/home/popularity")

    def del_popularity(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Popularity.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/popularity")

    def update_popularity(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Popularity.objects.get(id=update_int)
            update_data.object_id = Event.objects.get(id=request.POST.get("object_id"))
            update_data.date = request.POST.get("date")
            update_data.number_of_visitors = request.POST.get("number_of_visitors")
            update_data.save()
            return HttpResponseRedirect("/home/popularity")

def index_user(request):
    index_form = DataUsers()
    index_data = Users.objects.all()
    return render(request, "firstapp/Template_user.html", {"form": index_form, "data": index_data})

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            add_data = Users()
            add_data.number = request.POST.get("number")
            add_data.name = request.POST.get("name")
            add_data.position = request.POST.get("position")
            add_data.save()
            return HttpResponseRedirect("/home/users")

    def del_user(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Users.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/users")

    def update_user(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Users.objects.get(id=update_int)
            update_data.number = request.POST.get("number")
            update_data.name = request.POST.get("name")
            update_data.position = request.POST.get("position")
            update_data.save()
            return HttpResponseRedirect("/home/users")