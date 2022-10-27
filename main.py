from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from database import MyDB
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.widget import MDWidget
"""
    Gia to kalo tou sanity mou kalo tha itan na dimiourgisw allo python arxeio to opoio tha diaxeirizete to mysql,
    giati an to kanw auto edw tha mou gamithei i logiki poli asxima :D
"""

Window.size = (300, 500)

#Database handling class created by yours beautifully. More methods to come soon :(
global mydb

mydb = MyDB()

"""
    TODO LIST        
        1) min asxolitheis kan me to mysql aksizeis kalitera stin zwi
        2) ftiakse to background color tou splash art na einai idio me to gif na min einai asximo ;D
        2) kali tixi

        MDTopAppBar:
            id: username_topappbar
            title: ""
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open"), "Menu"]]
            elevation: 10
            specific_text_color: 1,1,1,1
            md_bg_color: 0.10980392156862745,0.10196078431372549,0.10980392156862745, 1

"""
class InformationWidget(MDWidget):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file('splashart.kv'))
        self.sm.add_widget(Builder.load_file('user.kv'))
        self.sm.add_widget(Builder.load_file('login.kv')) 
        return self.sm
    
    def logger(self):
        password = self.sm.get_screen('loginpage').ids.login.text
        mydb.cur.execute(f"SELECT * FROM customers WHERE password='{password}'")
        self.res = mydb.cur.fetchall()
        user_info = self.sm.get_screen('user_screen').ids
        print(self.res)
        if len(self.res) == 0:
            #This should make a popup where it informs the user that the password was wrong
            button = MDRectangleFlatButton(text="CLOSE", on_release=lambda x: self.close_dialog(x))
            self.dialog = MDDialog(
                title="ERROR!", 
                type="alert", 
                text="Password is incorrect or the user does not exist!", 
                buttons=[button], 
                size_hint=(0.7, None)
            )
            self.dialog.open()
            
        else:
            self.change_screen('user_screen', 'left')
            user_info.balance.text = f"Balance: {self.res[0][3]}"
            user_info.address.text = f"Address: {self.res[0][1]}"
            user_info.internet_speed.text = f"Internet Speed: {self.res[0][4]}"
            user_info.user_name.title = f"Hi, {self.res[0][0]}" # This is used to grab the input provided by the user and set it as a title in the MDTopAppBar of the UserScreen. This should be used as a way to access the name of a customer and set as greeting in the title of their personal user page


    def close_dialog(self, obj):
        self.dialog.dismiss()            
    
    def change_screen(self, screen_choice, direction_choice):
        
        self.sm.current = screen_choice
        self.sm.transition.direction = direction_choice
        print('button works!') 

    def splash_screen_start(self, *args):
        self.sm.current = 'loginpage'

    def on_start(self):
        
        Clock.schedule_once(self.splash_screen_start, 2)
        #self.fps_monitor_start()        
    
if __name__ == "__main__":
    MainApp().run()
