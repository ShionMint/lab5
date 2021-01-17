from django.test import TestCase
import unittest
from firstapp.models import Owner, Object, Event, Popularity, Users, Backup_copy

class OwnerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Owner.objects.create(type_owner='Юр. лицо', name_owner='ООО Рога и копыта', full_name='Венедиктов И.С.', contact_number='+79523084233', opening_date='2017-03-03')

    def test_type_owner_label(self):
        ad = Owner.objects.get(id=1)
        field_label = ad._meta.get_field('type_owner').verbose_name
        self.assertEquals(field_label, 'type_owner')

    def test_name_owner_label(self):
        ad = Owner.objects.get(id=1)
        field_label = ad._meta.get_field('name_owner').verbose_name
        self.assertEquals(field_label, 'name_owner')

    def test_full_name_label(self):
        ad = Owner.objects.get(id=1)
        field_label = ad._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full_name')

    def test_contact_number_label(self):
        ad = Owner.objects.get(id=1)
        field_label = ad._meta.get_field('contact_number').verbose_name
        self.assertEquals(field_label, 'contact_number')

    def test_opening_date_label(self):
        ad = Owner.objects.get(id=1)
        field_label = ad._meta.get_field('opening_date').verbose_name
        self.assertEquals(field_label, 'opening_date')

class ObjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Object.objects.create(owner_id='1', name='Искра', type='Клуб', address='г. Мирный, ул. Ильича, 2', number_of_seats='24')

    def test_owner_id_label(self):
        ad = Object.objects.get(id=1)
        field_label = ad._meta.get_field('owner_id').verbose_name
        self.assertEquals(field_label, 'owner_id')

    def test_name_label(self):
        ad = Object.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_type_label(self):
        ad = Object.objects.get(id=1)
        field_label = ad._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_address_label(self):
        ad = Object.objects.get(id=1)
        field_label = ad._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_number_of_seats_label(self):
        ad = Object.objects.get(id=1)
        field_label = ad._meta.get_field('number_of_seats').verbose_name
        self.assertEquals(field_label, 'number_of_seats')

class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(owner_id='1', date_of_event='2017-01-01', type_of_event='Концерт')

    def test_owner_id_label(self):
        ad = Event.objects.get(id=1)
        field_label = ad._meta.get_field('owner_id').verbose_name
        self.assertEquals(field_label, 'owner_id')

    def test_date_of_event_label(self):
        ad = Event.objects.get(id=1)
        field_label = ad._meta.get_field('date_of_event').verbose_name
        self.assertEquals(field_label, 'date_of_event')

    def test_type_of_event_label(self):
        ad = Event.objects.get(id=1)
        field_label = ad._meta.get_field('type_of_event').verbose_name
        self.assertEquals(field_label, 'type_of_event')

class PopularityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Popularity.objects.create(object_id='1', date='2017-01-01', number_of_visitors='20')

    def test_object_id_label(self):
        ad = Popularity.objects.get(id=1)
        field_label = ad._meta.get_field('object_id').verbose_name
        self.assertEquals(field_label, 'object_id')

    def test_date_label(self):
        ad = Popularity.objects.get(id=1)
        field_label = ad._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_number_of_visitors_label(self):
        ad = Popularity.objects.get(id=1)
        field_label = ad._meta.get_field('number_of_visitors').verbose_name
        self.assertEquals(field_label, 'number_of_visitors')

class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(number='1', name='Ярослав И.М.', position='Работник', login='user1', password='123456')

    def test_number_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_position_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_login_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

class Backup_copyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(number='1', name='2017-01-01-backup')

    def test_number_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

