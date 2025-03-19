from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.telaDeInicializacao import TelaDeInicializacao
from screens.telaPedidos import TelaPedidos
from kivy.core.window import Window

class GerenciadorTelas(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TelaDeInicializacao(name="inicializacao"))
        self.add_widget(TelaPedidos(name="pedidos"))

class MeuApp(App):
    def build(self):
        Window.size = (360, 800)
        return GerenciadorTelas()

if __name__ == "__main__":
    MeuApp().run()
