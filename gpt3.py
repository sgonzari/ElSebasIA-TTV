import os
import openai
from dotenv import load_dotenv

# Cargar el fichero .env
load_dotenv()

# Cargar la key de OpenAI
openai.api_key = os.environ.get("OPENAI_KEY")

# Función que recibe el mensaje a enviar y devuelve la respuesta de GPT-3
def gpt3_request(message):
    # Guarda la respuesta de GPT-3
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo', # Motor seleccionado de OpenAI
        messages = message, # Mensaje a enviar
        temperature = 1, # Aleatoriedad en las respuestas
        max_tokens = 150, # Máximos tokens a retirar de la cuenta de OpenAI
        frequency_penalty = 2.0,
        presence_penalty = 2.0
    )

    return response['choices'][0]['message']['content'].strip()