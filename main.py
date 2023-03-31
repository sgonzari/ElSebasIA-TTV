import os
from gpt3 import *
from utils import *
from dotenv import load_dotenv
from twitchio.ext import commands

class Bot(commands.Bot):

    # Variable donde guardar los mensajes a enviar
    conversation = list()

    # Inicialización de la clase Bot
    def __init__ (self):
        super().__init__(
            token = os.environ.get("TWITCH_TOKEN"), 
            prefix = '!',
            initial_channels = [os.environ.get("TWITCH_CHANNEL")]
        )
        Bot.conversation.append({
            'role': 'system', 
            'content': open_file('prompt.txt') 
        })

    # Cuando el Bot está listo realiza lo que hay dentro
    async def event_ready (self):
        os.system('cls' if os.name=='nt' else 'clear')

        start_print()
        start_file()

    # Cuando capta un mensaje llama a esta función
    async def event_message (self, message):
        # Comprueba si el mensaje ha expirado
        if (expired_message(message.timestamp)):
            return
        # Comprueba si el mensaje ha sido enviado por un bot
        if (message.echo):
            return
        # Comprueba si el mensaje no es tan largo
        if (len(message.content) > 50):
            return

        # Imprime por consola el mensaje recibido
        print(f'<= | {message.author.name}: {message.content}')

        # Guarda en el log el mensaje recibido
        save_in_log(f'<= | {message.author.name}: {message.content} \n')

        # Manda a GPT-3 el mensaje recibido
        Bot.conversation.append({
            'role': 'user',
            'content': message.content.encode(encoding='ASCII',errors='ignore').decode()
        })

        # Recoge la respuesta de GPT-3
        response = gpt3_request(Bot.conversation)

        # Imprime por consola la respuesta de GPT-3
        print(f'=> | ElSebasIA: {response}')

        # Guarda en el log la respuesta de GPT-3
        save_in_log(f'=> | ElSebasIA: {response} \n')

        # Imprime por consola una distinción
        print("--------------------------------------------------------")

        # Guarda en el log una distinción
        save_in_log("-------------------------------------------------------- \n")


# Guarda en una variable del sistema la KEY de Google para el TTS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.environ.get("GOOGLE_KEY")
# Instancio la clase Bot
SebasIA = Bot()
# Arranco la clase Bot
SebasIA.run()