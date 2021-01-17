from django.test import TestCase
import unittest
from firstapp.models import Owner, Object, Event, Popularity, Users, Backup_copy
from django.urls import reverse

class View_Owner_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Owner.objects.create(type_owner='Юр. лицо', name_owner='ООО Рога и копыта', full_name='Венедиктов И.С.',
                             contact_number='+79523084233', opening_date='2017-03-03')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/owner/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('owner'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('owner'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_owner.html')

class View_Object_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Object.objects.create(owner_id='1', name='Искра', type='Клуб', address='г. Мирный, ул. Ильича, 2',
                              number_of_seats='24')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/object/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('object'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('object'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_object.html')

class View_Event_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(owner_id='1', date_of_event='2017-01-01', type_of_event='Концерт')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/event/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('event'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('event'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_event.html')

class View_Popularity_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Popularity.objects.create(object_id='1', date='2017-01-01', number_of_visitors='20')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/popularity/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('popularity'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('popularity'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_popularity.html')

class View_Users_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(number='1', name='Ярослав И.М.', position='Работник', login='user1', password='123456')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_user.html')

class View_Backup_copy_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(number='1', name='2017-01-01-backup')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/backup/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('backup'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('backup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_backup.html')