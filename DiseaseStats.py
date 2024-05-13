from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
Window.clearcolor = (0.97, 0.92, 0.9, 1)


class FeedbackToPatient(MDApp):
    def build(self):
        return Builder.load_file('DiseaseStats.kv')


FeedbackToPatient().run()