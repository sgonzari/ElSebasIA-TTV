import os
from google.cloud import texttospeech_v1beta1 as texttospeech
import vlc
import time

def tts_play (response):
    # Inicializa el TextToSpeech
    client = texttospeech.TextToSpeechClient()

    # Formaliza el texto a enviar al TextToSpeech
    ssml_text = '<speak>'
    response_counter = 0
    mark_array = []
    for s in response.split(' '):
        ssml_text += f'<mark name="{response_counter}"/>{s}'
        mark_array.append(s)
        response_counter += 1
    ssml_text += '</speak>'

    # Sintetiza el texto
    input_text = texttospeech.SynthesisInput(ssml = ssml_text)

    # Configuración de la voz del TextToSpeech
    # https://cloud.google.com/text-to-speech/docs/voices
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-ES",
        name= "es-ES-Wavenet-B",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )

    # Configuración del encoding a obtener
    audio_config = texttospeech.AudioConfig(    
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )
    
    # Recibe el TextToSpeech
    response = client.synthesize_speech(
        request={
            "input": input_text, 
            "voice": voice, 
            "audio_config": audio_config, 
            "enable_time_pointing": ["SSML_MARK"]
        }
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)

    audio_file = os.path.dirname(__file__) + '\output.mp3'
    
    media = vlc.MediaPlayer(audio_file)
    media.play()

    count = 0
    current = 0
    for i in range(len(response.timepoints)):
        count += 1
        current += 1

        with open("output.txt", "a", encoding="utf-8") as out:
            out.write(mark_array[int(response.timepoints[i].mark_name)] + " ")

        if i != len(response.timepoints) - 1:
            total_time = response.timepoints[i + 1].time_seconds
            time.sleep(total_time - response.timepoints[i].time_seconds)

        if current == 25:
                open('output.txt', 'w', encoding="utf-8").close()
                current = 0
                count = 0

        elif count % 7 == 0:
            with open("output.txt", "a", encoding="utf-8") as out:
                out.write("\n")

    time.sleep(2)
    open('output.txt', 'w').close()

    os.remove(audio_file)