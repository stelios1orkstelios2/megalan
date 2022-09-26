from cgitb import text
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar

class UserScreen(Screen):
    pass # Den exw idea pws ston poutso na to ftiaksw auto akoma 
"""
    TODO LIST
        1) katse na katalabeis pws ston poutso douleuoun ta screens 
        2) min asxolitheis kan me to mysql aksizeis kalitera stin zwi
        3) kali tixi

"""

class LoginScreen(Screen):
    pass

Builder.load_file('user.kv')
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        self.sm = ScreenManager()
        self.sm.add_widget(UserScreen(name='user_screen'))
        self.sm.add_widget(LoginScreen(name='loginpage'))
        self.sm.current = 'loginpage'
        menu_items = [
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Log Out",
                        "height": dp(56),
                        "on_release": lambda x="": self.menu_callback(x),
                    } 
                ]
        self.menu = MDDropdownMenu(items=menu_items, position="bottom", width_mult=4, ver_growth='down', hor_growth="right")
        return self.sm
    
    def change_screen(self):
        self.sm.current = 'user_screen'
        self.sm.transition.direction = 'left'
        print('button works!')
    
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()
    
    def menu_callback(self, text_item):
        self.sm.current = 'loginpage'
        self.menu.dismiss()
        
    def on_start(self):
        self.fps_monitor_start()        
"""
    OTAN ME TO KALO FTASOUME STO SIMEIO NA ASXOLITHOUME ME TIN ACTUAL DIADIKASIA 

    def logger(self):
       login = self.root.ids.login.text
"""
        


if __name__ == "__main__":

    MainApp().run()
