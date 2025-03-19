from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp

# Criando um botão baseado em imagem
class BotaoImagem(ButtonBehavior, Image):
    pass

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        # Barra Superior (Botões "Sair" e "Menu")
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            padding: dp(10)

            BotaoImagem:
                source: "assets/botaoSairApp.png"
                size_hint_x: None
                width: dp(50)
                on_release: app.root.current = "inicializacao"

            Widget:  # Espaço entre os botões

            BotaoImagem:
                source: "assets/botaoMenuApp.png"
                size_hint_x: None
                width: dp(50)
                on_release: app.root.current = "menu_opcoes"

        # Categorias
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)

            Button:
                text: "🍽️ Pratos Principais"
                on_release: root.mostrar_categoria("pratos_principais")

            Button:
                text: "🥤 Bebidas"
                on_release: root.mostrar_categoria("bebidas")

            Button:
                text: "🍰 Sobremesas"
                on_release: root.mostrar_categoria("sobremesas")

            Button:
                text: "🍔 Lanches"
                on_release: root.mostrar_categoria("lanches")

        # Lista de Pratos (que muda dinamicamente)
        ScrollView:
            GridLayout:
                id: lista_pratos
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: dp(10)
'''

class TelaPedidos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pratos = {
            "pratos_principais": ["Strogonoff", "Parmegiana", "Filé de Peixe"],
            "bebidas": ["Refrigerante", "Suco Natural", "Cerveja"],
            "sobremesas": ["Pudim", "Bolo de Chocolate", "Sorvete"],
            "lanches": ["X-Burguer", "Hot Dog", "Beirute"]
        }
        self.add_widget(Builder.load_string(KV))

    def mostrar_categoria(self, categoria):
        lista_pratos = self.ids.lista_pratos
        lista_pratos.clear_widgets()
        
        for prato in self.pratos[categoria]:
            lista_pratos.add_widget(
                Button(
                    text=prato,
                    size_hint_y=None,
                    height=dp(50),
                    background_color=(0.2, 0.6, 0.2, 1)
                )
            )
