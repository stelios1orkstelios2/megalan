from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="B202d6178",
    database='users'
)
cur = mydb.cursor()


Window.size = (300, 500)


#class SplashScreen(Screen):
#    pass

"""
    TODO LIST        
        1) min asxolitheis kan me to mysql aksizeis kalitera stin zwi
        2) ftiakse to background color tou splash art na einai idio me to gif na min einai asximo ;D
        2) kali tixi

"""

class MainApp(MDApp):
    def build(self):
        
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file('splashart.kv'))
        self.sm.add_widget(Builder.load_file('user.kv'))
        self.sm.add_widget(Builder.load_file('main.kv'))
        """
        FOR MENU IN TOPAPPBAR OF USERSCREEN
        menu_items = [
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Log Out",
                        "height": dp(56),
                        "on_release": lambda x="": self.menu_callback(x),
                    } 
                ]
        self.menu = MDDropdownMenu(items=menu_items, position="bottom", width_mult=2, ver_growth='down', hor_growth="right")
        """
        
        
        return self.sm
    
    def change_screen(self, screen_choice, direction_choice):
        self.sm.current = screen_choice
        self.sm.transition.direction = direction_choice
        if self.sm.get_screen('loginpage').ids.login.text.upper() == "":
            self.sm.get_screen('user_screen').ids.username_topappbar.title = "No user!"
        else:
            self.sm.get_screen('user_screen').ids.username_topappbar.title = f"Hi, {self.sm.get_screen('loginpage').ids.login.text.upper()}" # This is used to grab the input provided by the user and set it as a title in the MDTopAppBar of the UserScreen. This should be used as a way to access the name of a customer and set as greeting in the title of their personal user page
        print('button works!') # Used for debuggin purposes 
    
    def logout_button(self, button):
        self.change_screen('loginpage', 'right')
        
    
    def menu_callback(self, text_item):
        self.change_screen('loginpage', 'right')
        self.menu.dismiss()
    
    def splash_screen_start(self, *args):
        self.sm.current = 'loginpage'

    def on_start(self):
        
        Clock.schedule_once(self.splash_screen_start, 7)
        #self.fps_monitor_start()        
"""
    OTAN ME TO KALO FTASOUME STO SIMEIO NA ASXOLITHOUME ME TIN ACTUAL DIADIKASIA 

    def logger(self):
       login = self.root.ids.login.text
"""
        


if __name__ == "__main__":
    MainApp().run()
