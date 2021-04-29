from kivy.app import App
from kivy.uix.button import Button

DATOS_MENSAJES = {
    "nombre": "AJJAJAJAJAJAJAJAJA",
    "mensaje-saludo": "Hola Misión TIC 2022... soy ",
    "mensaje-no-inicio": "Hola, aún no es Misión TIC, soy "
}
MISION_TIC_2022 = True

if MISION_TIC_2022:
    pantalla = DATOS_MENSAJES["mensaje-saludo"] + DATOS_MENSAJES["nombre"]
else: 
    pantalla = DATOS_MENSAJES["mensaje-no-inicio"] + DATOS_MENSAJES["nombre"]


class TestApp(App):
    def build(self):
        return Button(text=pantalla)

TestApp().run()
