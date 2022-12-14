from kivy.app import App
import openai

# API de la cuenta de OpenAI para acceder a GPT3
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class MainApp(App):
    # Hacemos una variable de tipo STR donde guardaremos la conversación
    conversation_ant = ""

    def set_text(self):
        # Generamos la variable conversación
        conversation = ""
        # A la variable question le damos el valor str del textinput kivy
        my_textinput = self.root.ids.my_textinput

        # Le damos un Input a ChatGPT para que entienda que es una conversación
        # Y al principio le damos la conversación anterior
        conversation += self.conversation_ant + "\n\nHumano: " + my_textinput.text + "\n\nAI:"

        # Parametros de openai para la entrega del Input
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=conversation,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", " Humano:", " AI:"]
        )
        # Salida del ChatGPT, nos quedamos con el texto
        anwer = response.choices[0].text.strip()

        # Definimos el cuadro label kivy de marcado de texto y le pasamos de forma bonita el texto esrcito humano
        # mas el texto que recibimos de la IA
        my_label = self.root.ids["my_label"]
        my_label.text += "\n\n" + "Humano: " + my_textinput.text + "\n\n" + "AI: "+ anwer
        # La misma plantilla que sacamos por pantalla la gaurdamos en una variable de tipo STR
        self.conversation_ant += "\n\n" + "Humano: " + my_textinput.text + "\n\n" + "AI: "+ anwer

        pass

# Inicialización de la Classe
MainApp().run()
