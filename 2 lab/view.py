from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "700")

Window.clearcolor = (.80, .242, .126, 1)


class Felix(MDApp):
    def __init__(self, model, controller):
        super().__init__()
        self.controller = controller
        self.controller.setView(self)
        self.model = model
        self.number_record_per_page = 5
        self.number_record = 0
        self.number_page = 1
        self.current_page = 1
        self.search = Search()
        self.search.setController(controller)
        self.buffer = None

    def on_save_date(self, instance, value, date_range):
        self.buffer.text = value.strftime('%d.%m.%Y')

    def date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_date)
        date_dialog.open()

    def count_number_page(self):
        self.number_page = self.number_record // self.number_record_per_page
        if self.number_record % self.number_record_per_page > 0:
            self.number_page += 1

    def show_data(self):
        self.clear_label()

        x = self.root.ids.display_data_screen.ids.gl_2

        n = (self.current_page - 1) * self.number_record_per_page

        for j in range(self.number_record_per_page):
            dctnry = self.model.get_data()
            if len(dctnry) <= j:
                for k in range(5):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 500 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(5):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 500 / self.number_record_per_page)))
            else:
                x.add_widget(
                    Label(text=dctnry[j + n][0], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][2], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][3], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][4], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))

        self.root.ids.display_data_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.display_data_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def spinner_clicked(self, textinput_name, spinner):
        textinput_name.text = spinner.text

    def exit(self):
        self.stop()

    def to_first_page(self, current_page):
        self.current_page = 1
        current_page.text = str(self.current_page)
        self.show_data()

    def to_last_page(self, current_page):
        dctnry = self.model.get_data()
        self.current_page = len(dctnry) // self.number_record_per_page + 1
        current_page.text = str(self.current_page)
        self.show_data()

    def to_x_page(self, current_page, sign):
        dctnry = self.model.get_data()
        if sign == '+':
            if (len(dctnry) // self.number_record_per_page) >= self.current_page:
                self.current_page += 1
                current_page.text = str(self.current_page)
        elif sign == '-':
            if self.current_page - 1 > 0:
                self.current_page -= 1
                current_page.text = str(self.current_page)
        self.show_data()

    def clear_label(self):
        x = self.root.ids.display_data_screen.ids.gl_2
        x.clear_widgets()

    def to_x_record(self, num):
        self.clear_label()
        self.number_record_per_page = num
        self.count_number_page()
        self.show_data()

    def build(self):
        root = Builder.load_file('lib.kv')
        return root


class Search:
    def __init__(self):
        self.dctnry = {}
        self.number_record_per_page = 5
        self.number_record = 0
        self.number_page = 1
        self.current_page = 1

    def setController(self, controller):
        self.controller = controller

    def f_search(self, textinput_name, date, status, gl, new_dictionary, record, page):
        self.dctnry = self.controller.f_search(textinput_name, date, status)
        self.show_data(gl, record, page)

    def s_search(self, textinput_name, date, status, gl, new_dictionary, record, page):
        self.dctnry = self.controller.s_search(textinput_name, date, status)
        self.show_data(gl, record, page)

    def t_search(self, textinput, status, gl, new_dictionary, record, page):
        self.dctnry = self.controller.t_search(textinput, status)
        self.show_data(gl, record, page)

    def show_data(self, gl, record, page):
        x = gl
        x.clear_widgets()

        n = (self.current_page - 1) * self.number_record_per_page

        for j in range(self.number_record_per_page):
            if len(self.dctnry) <= j:
                for k in range(5):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 500 / self.number_record_per_page)))
            elif n + j >= len(self.dctnry):
                for k in range(5):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 500 / self.number_record_per_page)))
            else:
                x.add_widget(
                    Label(text=self.dctnry[j + n][0], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=self.dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=self.dctnry[j + n][2], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=self.dctnry[j + n][3], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=self.dctnry[j + n][4], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 500 / self.number_record_per_page)))

        record.text = "Кол-во записей: " + str(len(self.dctnry))
        self.number_record = len(self.dctnry)
        page.text = str(len(self.dctnry) // self.number_record_per_page + 1)

    def to_x_page(self, current_page, sign, gl, record, page):
        if sign == '+':
            if (len(self.dctnry) // self.number_record_per_page) >= self.current_page:
                self.current_page += 1
                current_page.text = str(self.current_page)
        elif sign == '-':
            if self.current_page - 1 > 0:
                self.current_page -= 1
                current_page.text = str(self.current_page)

        self.show_data(gl, record, page)

    def to_first_page(self, current_page, gl, record, page):
        self.current_page = 1
        current_page.text = str(self.current_page)
        self.show_data(gl, record, page)

    def to_last_page(self, current_page, gl, record, page):
        self.current_page = len(self.dctnry) // self.number_record_per_page + 1
        current_page.text = str(self.current_page)
        self.show_data(gl, record, page)

    def to_x_record(self, num, gl, record, page):
        gl.clear_widgets()
        self.number_record_per_page = num
        self.count_number_page()
        self.show_data(gl, record, page)

    def count_number_page(self):
        self.number_page = self.number_record // self.number_record_per_page
        if self.number_record % self.number_record_per_page > 0:
            self.number_page += 1

    def clear(self):
        self.dctnry = {}
        self.number_record_per_page = 5
        self.number_record = 0
        self.number_page = 1
        self.current_page = 1

class DisplayDataScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass