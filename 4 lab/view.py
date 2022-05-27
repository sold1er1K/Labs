from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "700")

Window.clearcolor = (.61, .87, .95, 1)


class Garden(MDApp):
    def __init__(self, model, controller):
        super().__init__()
        self.controller = controller
        self.controller.setView(self)
        self.model = model
        self.money = 99

    def exit(self):
        self.stop()

    def build(self):
        root = Builder.load_file('lib.kv')
        return root

    def clear_label(self):
        x = self.root.ids.display_data_screen.ids.gl_2
        x.clear_widgets()

    def update_data(self):
        self.root.ids.main_screen.ids.weather.text = "Погода: " + str(self.model.get_weather())
        self.root.ids.main_screen.ids.tree_kol.text = "Кол-во деревьев: " + str(self.model.tree_kol())
        self.root.ids.main_screen.ids.money.text = "Деньги: " + str(self.model.money())
        self.root.ids.main_screen.ids.garden_bed_kol.text = "Кол-во грядок: " + str(self.model.garden_bed_kol())
        self.root.ids.main_screen.ids.day.text = "День: " + str(self.model.day())
        self.show_data()

    def show_data(self):
        st = self.model.show()
        lst = st.split('|')
        lst_new = []
        for i in range(len(lst)):
            if lst[i].find('===') == -1 and lst[i].find("----") == -1:
                lst_new.append(lst[i])

        self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/lol.png'
        self.root.ids.main_screen.ids.tree_1.background_color = 1, 1, 1, 1

        self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/lol.png'
        self.root.ids.main_screen.ids.tree_2.background_color = 1, 1, 1, 1

        self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/lol.png'
        self.root.ids.main_screen.ids.tree_3.background_color = 1, 1, 1, 1

        self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/lol.png'
        self.root.ids.main_screen.ids.tree_4.background_color = 1, 1, 1, 1

        self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/lol.png'
        self.root.ids.main_screen.ids.tree_5.background_color = 1, 1, 1, 1

        for i in range(len(lst_new)):
            if lst_new[i].find('Garden bed') != -1:
                st = lst_new[i].split()
                num = int(st[2])
                if num == 1:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_1.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_1.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_1.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_1.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_1.background_normal = ''
                        self.root.ids.main_screen.ids.cell_1.text = '1'
                        error = True
                        if lst_new[i+2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_1.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i+2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_1.background_color = 0, 1, 0, 1

                        if lst_new[i+3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_1.background_color = 0, 0, 0, 1

                        if lst_new[i+4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i+7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_1.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_1.background_color = 1, 1, 1, 1

                elif num == 2:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_2.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_2.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_2.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_2.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_2.background_normal = ''
                        self.root.ids.main_screen.ids.cell_2.text = '2'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_2.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_2.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_2.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_2.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_2.background_color = 1, 1, 1, 1

                elif num == 3:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_3.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_3.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_3.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_3.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_3.background_normal = ''
                        self.root.ids.main_screen.ids.cell_3.text = '3'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_3.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_3.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_3.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_3.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_3.background_color = 1, 1, 1, 1

                elif num == 4:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_4.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_4.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_4.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_4.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_4.background_normal = ''
                        self.root.ids.main_screen.ids.cell_4.text = '4'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_4.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_4.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_4.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_4.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_4.background_color = 1, 1, 1, 1

                elif num == 5:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_5.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_5.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_5.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_5.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_5.background_normal = ''
                        self.root.ids.main_screen.ids.cell_5.text = '5'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_5.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_5.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_5.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_5.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_5.background_color = 1, 1, 1, 11
                elif num == 6:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_6.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_6.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_6.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_6.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_6.background_normal = ''
                        self.root.ids.main_screen.ids.cell_6.text = '6'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_6.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_6.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_6.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_6.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_6.background_color = 1, 1, 1, 1

                elif num == 7:
                        error = False
                        if lst_new[i + 1] == 'tomato':
                            self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/tomato.png'
                            self.root.ids.main_screen.ids.cell_7.background_color = 1, 1, 1, 1
                        elif lst_new[i + 1] == 'potato':
                            self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/potato.png'
                            self.root.ids.main_screen.ids.cell_7.background_color = 1, 1, 1, 1
                        elif lst_new[i + 1] == 'pepper':
                            self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/pepper.png'
                            self.root.ids.main_screen.ids.cell_7.background_color = 1, 1, 1, 1
                        else:
                            self.root.ids.main_screen.ids.cell_7.background_color = .49, .69, .14, 1
                            self.root.ids.main_screen.ids.cell_7.background_normal = ''
                            self.root.ids.main_screen.ids.cell_7.text = '7'
                            error = True
                            if lst_new[i + 2] == 'Weed+':
                                self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/weed.png'
                                self.root.ids.main_screen.ids.cell_7.background_color = 1, 1, 1, 1

                        if not error:
                            if lst_new[i + 2] == 'Ill+':
                                self.root.ids.main_screen.ids.cell_7.background_color = 0, 1, 0, 1

                            if lst_new[i + 3] == 'Pest+':
                                self.root.ids.main_screen.ids.cell_7.background_color = 0, 0, 0, 1

                            if lst_new[i + 4] == 'Harvest+':
                                if lst_new[i + 1] == 'tomato':
                                    self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/tomato_harvest.png'

                                elif lst_new[i + 1] == 'potato':
                                    self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/potato_harvest.png'

                                elif lst_new[i + 1] == 'pepper':
                                    self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/pepper_harvest.png'

                            if lst_new[i + 7] == 'Weed+':
                                self.root.ids.main_screen.ids.cell_7.background_normal = 'pics/weed.png'
                                self.root.ids.main_screen.ids.cell_7.background_color = 1, 1, 1, 1

                elif num == 8:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_8.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_8.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_8.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_8.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_8.background_normal = ''
                        self.root.ids.main_screen.ids.cell_8.text = '8'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_8.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_8.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_8.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_8.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_8.background_color = 1, 1, 1, 1

                elif num == 9:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_9.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_9.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_9.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_9.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_9.background_normal = ''
                        self.root.ids.main_screen.ids.cell_9.text = '9'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_9.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_9.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_9.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_9.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_9.background_color = 1, 1, 1, 1

                elif num == 10:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_10.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_10.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_10.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_10.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_10.background_normal = ''
                        self.root.ids.main_screen.ids.cell_10.text = '10'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_10.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_10.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_10.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_10.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_10.background_color = 1, 1, 1, 1

                elif num == 11:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_11.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_11.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_11.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_11.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_11.background_normal = ''
                        self.root.ids.main_screen.ids.cell_11.text = '11'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_11.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_11.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_11.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_11.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_11.background_color = 1, 1, 1, 1

                elif num == 12:
                    error = False
                    if lst_new[i + 1] == 'tomato':
                        self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/tomato.png'
                        self.root.ids.main_screen.ids.cell_12.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'potato':
                        self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/potato.png'
                        self.root.ids.main_screen.ids.cell_12.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'pepper':
                        self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/pepper.png'
                        self.root.ids.main_screen.ids.cell_12.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.cell_12.background_color = .49, .69, .14, 1
                        self.root.ids.main_screen.ids.cell_12.background_normal = ''
                        self.root.ids.main_screen.ids.cell_12.text = '12'
                        error = True
                        if lst_new[i + 2] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_12.background_color = 1, 1, 1, 1

                    if not error:
                        if lst_new[i + 2] == 'Ill+':
                            self.root.ids.main_screen.ids.cell_12.background_color = 0, 1, 0, 1

                        if lst_new[i + 3] == 'Pest+':
                            self.root.ids.main_screen.ids.cell_12.background_color = 0, 0, 0, 1

                        if lst_new[i + 4] == 'Harvest+':
                            if lst_new[i + 1] == 'tomato':
                                self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/tomato_harvest.png'

                            elif lst_new[i + 1] == 'potato':
                                self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/potato_harvest.png'

                            elif lst_new[i + 1] == 'pepper':
                                self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/pepper_harvest.png'

                        if lst_new[i + 7] == 'Weed+':
                            self.root.ids.main_screen.ids.cell_12.background_normal = 'pics/weed.png'
                            self.root.ids.main_screen.ids.cell_12.background_color = 1, 1, 1, 1


            if lst_new[i].find('Tree') != -1:
                st = lst_new[i].split()
                num = int(st[1])
                if num == 1:
                    if lst_new[i + 1] == 'apple':
                        self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/apple_little.png'
                        self.root.ids.main_screen.ids.tree_1.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'peer':
                        self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/peer_little.png'
                        self.root.ids.main_screen.ids.tree_1.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/lol.png'
                        self.root.ids.main_screen.ids.tree_1.background_color = 1, 1, 1, 1

                    if lst_new[i + 2] == 'Ill+':
                        self.root.ids.main_screen.ids.tree_1.background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        self.root.ids.main_screen.ids.tree_1.background_color = 0, 0, 0, 1

                    if lst_new[i + 4] == 'Harvest+':
                        if lst_new[i + 1] == 'apple':
                            self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/apple.png'

                        elif lst_new[i + 1] == 'peer':
                            self.root.ids.main_screen.ids.tree_1.background_normal = 'pics/peer.png'

                if num == 2:
                    if lst_new[i + 1] == 'apple':
                        self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/apple_little.png'
                        self.root.ids.main_screen.ids.tree_2.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'peer':
                        self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/peer_little.png'
                        self.root.ids.main_screen.ids.tree_2.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/lol.png'
                        self.root.ids.main_screen.ids.tree_2.background_color = 1, 1, 1, 1

                    if lst_new[i + 2] == 'Ill+':
                        self.root.ids.main_screen.ids.tree_2.background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        self.root.ids.main_screen.ids.tree_2.background_color = 0, 0, 0, 1

                    if lst_new[i + 4] == 'Harvest+':
                        if lst_new[i + 1] == 'apple':
                            self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/apple.png'

                        elif lst_new[i + 1] == 'peer':
                            self.root.ids.main_screen.ids.tree_2.background_normal = 'pics/peer.png'

                if num == 3:
                    if lst_new[i + 1] == 'apple':
                        self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/apple_little.png'
                        self.root.ids.main_screen.ids.tree_3.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'peer':
                        self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/peer_little.png'
                        self.root.ids.main_screen.ids.tree_3.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/lol.png'
                        self.root.ids.main_screen.ids.tree_3.background_color = 1, 1, 1, 1

                    if lst_new[i + 2] == 'Ill+':
                        self.root.ids.main_screen.ids.tree_3.background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        self.root.ids.main_screen.ids.tree_3.background_color = 0, 0, 0, 1

                    if lst_new[i + 4] == 'Harvest+':
                        if lst_new[i + 1] == 'apple':
                            self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/apple.png'

                        elif lst_new[i + 1] == 'peer':
                            self.root.ids.main_screen.ids.tree_3.background_normal = 'pics/peer.png'

                if num == 4:
                    if lst_new[i + 1] == 'apple':
                        self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/apple_little.png'
                        self.root.ids.main_screen.ids.tree_4.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'peer':
                        self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/peer_little.png'
                        self.root.ids.main_screen.ids.tree_4.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/lol.png'
                        self.root.ids.main_screen.ids.tree_4.background_color = 1, 1, 1, 1

                    if lst_new[i + 2] == 'Ill+':
                        self.root.ids.main_screen.ids.tree_4.background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        self.root.ids.main_screen.ids.tree_4.background_color = 0, 0, 0, 1

                    if lst_new[i + 4] == 'Harvest+':
                        if lst_new[i + 1] == 'apple':
                            self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/apple.png'

                        elif lst_new[i + 1] == 'peer':
                            self.root.ids.main_screen.ids.tree_4.background_normal = 'pics/peer.png'

                if num == 5:
                    if lst_new[i + 1] == 'apple':
                        self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/apple_little.png'
                        self.root.ids.main_screen.ids.tree_5.background_color = 1, 1, 1, 1
                    elif lst_new[i + 1] == 'peer':
                        self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/peer_little.png'
                        self.root.ids.main_screen.ids.tree_5.background_color = 1, 1, 1, 1
                    else:
                        self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/lol.png'
                        self.root.ids.main_screen.ids.tree_5.background_color = 1, 1, 1, 1

                    if lst_new[i + 2] == 'Ill+':
                        self.root.ids.main_screen.ids.tree_5.background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        self.root.ids.main_screen.ids.tree_5.background_color = 0, 0, 0, 1

                    if lst_new[i + 4] == 'Harvest+':
                        if lst_new[i + 1] == 'apple':
                            self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/apple.png'

                        elif lst_new[i + 1] == 'peer':
                            self.root.ids.main_screen.ids.tree_5.background_normal = 'pics/peer.png'



class MainScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class GardenScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass
