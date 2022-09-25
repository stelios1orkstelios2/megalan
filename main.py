from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class UserPage(Screen):
    pass # Den exw idea pws ston poutso na to ftiaksw auto akoma 
"""
    TODO LIST
        1) katse na katalabeis pws ston poutso douleuoun ta screens 
        2) min asxolitheis kan me to mysql aksizeis kalitera stin zwi
        3) kali tixi

"""

class MainApp(MDApp):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(UserPage(name='User'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('my.kv')
        
    def logger(self):
        login = self.root.ids.login.text
        

    def on_start(self):
        self.fps_monitor_start()

MainApp().run()
