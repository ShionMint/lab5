from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from firstapp import views

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='accounts/login/')),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('home/', views.index, name='home'),

    # Добавление владельца
    path('home/owner/', views.index_owner, name='owner'),
    path('home/owner/add/', views.view_owner.add_owner, name='add_owner'),
    path('home/owner/del/', views.view_owner.del_owner, name='del_owner'),
    path('home/owner/update/', views.view_owner.update_owner, name='update_owner'),

    # Добавление объектов
    path('home/object/', views.index_object, name='object'),
    path('home/object/add/', views.view_oblect.add_object, name='add_object'),
    path('home/object/del/', views.view_oblect.del_object, name='del_object'),
    path('home/object/update/', views.view_oblect.update_object, name='update_object'),

    # Добавление мероприятий
    path('home/event/', views.index_event, name='event'),
    path('home/event/add/', views.view_event.add_event, name='add_event'),
    path('home/event/del/', views.view_event.del_event, name='del_event'),
    path('home/event/update/', views.view_event.update_event, name='update_event'),

    # Добавление информации о популярности
    path('home/popularity/', views.index_popularity, name='popularity'),
    path('home/popularity/add/', views.view_popularity.add_popularity, name='add_popularity'),
    path('home/popularity/del/', views.view_popularity.del_popularity, name='del_popularity'),
    path('home/popularity/update/', views.view_popularity.update_popularity, name='update_popularity'),

    # Добавление информации о пользователях
    path('home/users/', views.index_user, name='users'),
    path('home/users/add/', views.view_user.add_user, name='add_users'),
    path('home/users/del/', views.view_user.del_user, name='del_users'),
    path('home/users/update/', views.view_user.update_user, name='update_users'),

    # Добавление информации о пользователях
    path('home/backup/', views.index_backup, name='backup'),
    path('home/backup/add/', views.view_backup.add_backup, name='add_users'),
    path('home/backup/del/', views.view_backup.del_backup, name='del_users'),
    path('home/backup/update/', views.view_backup.update_backup, name='update_users'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
