from django.contrib import admin
from .models import Owner, Object, Event, Popularity, Users

# Register your models here.

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('type_owner','name_owner','full_name','contact_number','opening_date')

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name','type','address','number_of_seats')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date_of_event','type_of_event')

@admin.register(Popularity)
class PopularityAdmin(admin.ModelAdmin):
    list_display = ('date','number_of_visitors')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('number','name','position')

