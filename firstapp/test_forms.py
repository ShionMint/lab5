from django.test import TestCase
import unittest
from firstapp.forms import DateBackup, DataUsers, DataPopularity, DataEvent, DataOwner, DataObject

class DataOwnerFormTest(TestCase):

    def test_type_owner_label(self):
        form = DataOwner()
        self.assertTrue(form.fields['type_owner'].label == None or form.fields['type_owner'].label == 'Тип организации')

    def test_name_owner_label(self):
        form = DataOwner()
        self.assertTrue(form.fields['name_owner'].label == None or form.fields['name_owner'].label == 'Название организации')

    def test_full_name_label(self):
        form = DataOwner()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'ФИО')

    def test_contact_number_label(self):
        form = DataOwner()
        self.assertTrue(form.fields['contact_number'].label == None or form.fields['contact_number'].label == 'Конактный телефон')

    def test_opening_date_label(self):
        form = DataOwner()
        self.assertTrue(form.fields['opening_date'].label == None or form.fields['opening_date'].label == 'Дата открытия')

    def test_resoult(self):
        form = DataOwner(data={'type_owner': "Юр. лицо", 'name_owner': "ООО Рога и копыта", 'full_name': "Венедиктов И.С.", 'contact_number': "+79523084233", 'opening_date': "2017-03-03"})
        self.assertTrue(form.is_valid())

class DataObjectFormTest(TestCase):

    def test_owner_id_label(self):
        form = DataObject()
        self.assertTrue(form.fields['owner_id'].label == None or form.fields['owner_id'].label == 'Владелец')

    def test_name_label(self):
        form = DataObject()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название объекта')

    def test_type_label(self):
        form = DataObject()
        self.assertTrue(form.fields['type'].label == None or form.fields['type'].label == 'Тип объекта')

    def test_address_label(self):
        form = DataObject()
        self.assertTrue(form.fields['address'].label == None or form.fields['address'].label == 'Адресс объекта')

    def test_number_of_seats_label(self):
        form = DataObject()
        self.assertTrue(form.fields['number_of_seats'].label == None or form.fields['number_of_seats'].label == 'Число мест')

    def test_resoult(self):
        form = DataObject(data={'owner_id': 1, 'name': "Искра", 'type': "Клуб", 'address': "г. Мирный, ул. Ильича, 2", 'number_of_seats': "24"})
        self.assertTrue(form.is_valid())

class DataEventFormTest(TestCase):

    def test_object_id_label(self):
        form = DataEvent()
        self.assertTrue(form.fields['object_id'].label == None or form.fields['object_id'].label == 'Объект')

    def test_date_of_event_label(self):
        form = DataEvent()
        self.assertTrue(form.fields['date_of_event'].label == None or form.fields['date_of_event'].label == 'Дата мероприятия')

    def test_type_of_event_label(self):
        form = DataEvent()
        self.assertTrue(form.fields['type_of_event'].label == None or form.fields['type_of_event'].label == 'Тип мероприятия')

    def test_resoult(self):
        form = DataEvent(data={'object_id': 1, 'date_of_event': "2017-01-01", 'type_of_event': "Концерт"})
        self.assertTrue(form.is_valid())

class DataPopularityFormTest(TestCase):

    def test_object_id_label(self):
        form = DataPopularity()
        self.assertTrue(form.fields['object_id'].label == None or form.fields['object_id'].label == 'Объект')

    def test_date_label(self):
        form = DataPopularity()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата опроса')

    def test_number_of_visitors_label(self):
        form = DataPopularity()
        self.assertTrue(form.fields['number_of_visitors'].label == None or form.fields['number_of_visitors'].label == 'Число посетивших')

    def test_resoult(self):
        form = DataPopularity(data={'object_id': 1, 'date': "2017-01-01", 'number_of_visitors': "20"})
        self.assertTrue(form.is_valid())

class DataUserFormTest(TestCase):

    def test_number_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер пользователя')

    def test_name_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ФИО')

    def test_position_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_login_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'Логин')

    def test_password_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль')

    def test_resoult(self):
        form = DataUsers(data={'number': "1", 'name': "Ярослав И.М.", 'position': "Работник", 'login': "user1", 'password': "123456"})
        self.assertTrue(form.is_valid())

class DataBackupFormTest(TestCase):

    def test_number_label(self):
        form = DateBackup()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер резервной копии')

    def test_name_label(self):
        form = DateBackup()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название резервной копии')

    def test_resoult(self):
        form = DateBackup(data={'number': "1", 'name': "2017-01-01-backup"})
        self.assertTrue(form.is_valid())

