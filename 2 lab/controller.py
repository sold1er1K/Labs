import datetime


class Controller:
    def __init__( self, model):
        self.model = model

    def setView(self, view):
        self.view = view

    def save_to_file(self, file_name, status):
        symbols = set('!@#$%^&*()-+"№;%:?=/.,<>\|')
        k = 0
        for i in file_name.text:
            if i in symbols:
                k += 1
        if k > 0:
            status.text = 'Недопустимые смволы в названии'
        else:
            self.model.save_to_file(file_name.text)
            status.text = 'Сохранение выполнено'
            self.view.show_data()

    def add(self, input_name, input_date_of_birth, input_date_of_visit, input_veterinarian, input_diagnosis,
            status):
        if input_name.text == '':
            status.text = 'Поле "имя" незаполнено'
        elif input_date_of_birth.text == "Дата(вывести выбранную)":
            status.text = 'Поле "дата рождения" незаполнено'
        elif input_date_of_visit.text == 'Дата(вывести выбранную)':
            status.text = 'Поле "дата визита" незаполнено'
        elif input_veterinarian.text == '':
            status.text = 'Поле "ФИО ветеринара" незаполнено'
        elif input_diagnosis.text == '':
            status.text = 'Поле "фраза из диагноза" незаполнено'
        elif datetime.datetime.strptime(input_date_of_visit.text, '%d.%m.%Y').date() < datetime.datetime.strptime(input_date_of_birth.text, '%d.%m.%Y').date():
            status.text = 'Некорректно введённые даты'
        else:
            status.text = 'Добавление выполнено'
            self.model.add(input_name.text, input_date_of_birth.text, input_date_of_visit.text, input_veterinarian.text, input_diagnosis.text)
            self.view.show_data()

    def load_to_dctnry(self, button=None):
        self.model.load_to_dctnry()
        button.disabled = True
        self.view.show_data()

    def t_dell(self, textinput, status):
        if textinput.text == '':
            status.text = 'Поле "фразва из диагноза" не заполнено'
        else:
            k = self.model.t_dell(textinput)
            if k > 0:
                status.text = 'Удалено {} записи(ей)'.format(k)
            else:
                status.text = 'Записей не найдено'
            self.view.show_data()

    def s_dell(self, textinput, date, status):
        if textinput.text == '':
            status.text = 'Поле "ФИО ветеринара" не заполнено'
        elif date.text == 'Дата(вывести выбранную)':
            status.text = 'Поле "дата визита" не заполнено'
        elif datetime.datetime.strptime(date.text, '%d.%m.%Y').date() > datetime.date.today():
            status.text = 'Неверная дата'
        else:
            k = self.model.s_dell(textinput, date)
            if k > 0:
                status.text = 'Удалено {} записи(ей)'.format(k)
            else:
                status.text = 'Записей не найдено'
            self.view.show_data()

    def f_dell(self, textinput, date, status):
        if textinput.text == '':
            status.text = 'Поле "имя" не заполнено'
        elif date.text == 'Дата(вывести выбранную)':
            status.text = 'Поле "дата рождения" не заполнено'
        elif datetime.datetime.strptime(date.text, '%d.%m.%Y').date() > datetime.date.today():
            status.text = 'Неверная дата'
        else:
            k = self.model.f_dell(textinput, date)
            if k > 0:
                status.text = 'Удалено {} записи(ей)'.format(k)
            else:
                status.text = 'Записей не найдено'
        self.view.show_data()

    def selected(self, filename, label, button):
        if filename[0].find('xml', -3) == -1:
            label.text = 'Выберите xml файл!'
            button.disabled = True
        else:
            label.text = ''
            self.model.set_filename(filename[0])
            button.disabled = False

    def f_search(self, textinput_name, date, status):
        info = {}
        if textinput_name.text == '':
            status.text = 'Поле "имя" не заполнено'
        elif date.text == 'Дата(вывести выбранную)':
            status.text = 'Поле "дата рождения" не заполнено'
        elif datetime.datetime.strptime(date.text, '%d.%m.%Y').date() > datetime.date.today():
            status.text = 'Неверная дата'
        else:
            info, k = self.model.f_search(textinput_name, date)
            status.text = 'Найдено {} записи(ей)'.format(k)
        return info

    def s_search(self, textinput_name, date, status):
        info = {}
        if textinput_name.text == '':
            status.text = 'Поле "ФИО ветеринара" не заполнено'
        elif date.text == 'Дата(вывести выбранную)':
            status.text = 'Поле "дата визита" не заполнено'
        elif datetime.datetime.strptime(date.text, '%d.%m.%Y').date() > datetime.date.today():
            status.text = 'Неверная дата'
        else:
            info, k = self.model.s_search(textinput_name, date)
            status.text = 'Найдено {} записи(ей)'.format(k)
        return info

    def t_search(self, textinput, status):
        info = {}
        if textinput.text == '':
            status.text = 'Поле "фраза из диагноза" не заполнено'
        else:
            info, k = self.model.t_search(textinput)
            status.text = 'Найдено {} записи(ей)'.format(k)
        return info