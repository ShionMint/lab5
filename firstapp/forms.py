from django import forms
from .models import Owner, Event, Object, Popularity, Users

class DataOwner(forms.Form):
    type_owner = forms.CharField(label="Тип организации")
    name_owner = forms.CharField(label="Название организации")
    full_name = forms.CharField(label="ФИО")
    contact_number = forms.CharField(label="Конактный телефон")
    opening_date = forms.DateField(label="Дата открытия")

class DataObject(forms.Form):
    owner_id = forms.ModelChoiceField(label="Владелец", queryset=Owner.objects.all().order_by('id'))
    name = forms.CharField(label="Название объекта")
    type = forms.CharField(label="Тип объекта")
    address = forms.CharField(label="Адресс объекта")
    number_of_seats = forms.IntegerField(label="Число мест")

class DataEvent(forms.Form):
    object_id = forms.ModelChoiceField(label="Объект", queryset=Object.objects.all().order_by('id'))
    date_of_event = forms.DateField(label="Дата мероприятия")
    type_of_event = forms.CharField(label="Тип мероприятия")

class DataPopularity(forms.Form):
    object_id = forms.ModelChoiceField(label="Объект", queryset=Object.objects.all().order_by('id'))
    date = forms.DateField(label="Дата опроса")
    number_of_visitors = forms.IntegerField(label="Число посетивших")

class DataUsers(forms.Form):
    number = forms.IntegerField(label="Номер пользователя")
    name = forms.CharField(label="ФИО")
    position = forms.CharField(label="Должность")

