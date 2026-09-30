from kivy.app import App
from kivy.uix.button import Button

class GameApp(App):
    def build(self):
        self.btn = Button(text='Mujhe Dabao!', font_size=32)
        self.btn.bind(on_press=self.khel_shuru)
        return self.btn

    def khel_shuru(self, instance):
        self.btn.text = "Aapne Jeet Liya!"

if __name__ == '__main__':
    GameApp().run()
