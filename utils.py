import os
import datetime 

DIFFERENCE_TIME = 1

# Función para imprimir por pantalla el starting de la IA
def start_print ():
    print("--------------------------------------------------------")
    print(f"  ______ _  _____      _               _____           ")
    print(f" |  ____| |/ ____|    | |             |_   _|   /\     ")
    print(f" | |__  | | (___   ___| |__   __ _ ___  | |    /  \    ")
    print(f" |  __| | |\___ \ / _ \ '_ \ / _` / __| | |   / /\ \   ")
    print(f" | |____| |____) |  __/ |_) | (_| \__ \_| |_ / ____ \  ")
    print(f" |______|_|_____/ \___|_.__/ \__,_|___/_____/_/    \_\ ")
    print(f"                                                       ")
    print("--------------------------------------------------------")
    print(f"                                                       ")

# Función para escribir en el fichero del log el starting de la IA
def start_file ():
    save_in_log("-------------------------------------------------------- \n")
    save_in_log(f"  ______ _  _____      _               _____            \n")
    save_in_log(f" |  ____| |/ ____|    | |             |_   _|   /\      \n")
    save_in_log(f" | |__  | | (___   ___| |__   __ _ ___  | |    /  \     \n")
    save_in_log(f" |  __| | |\___ \ / _ \ '_ \ / _` / __| | |   / /\ \    \n")
    save_in_log(f" | |____| |____) |  __/ |_) | (_| \__ \_| |_ / ____ \   \n")
    save_in_log(f" |______|_|_____/ \___|_.__/ \__,_|___/_____/_/    \_\  \n")
    save_in_log(f"                                                        \n")
    save_in_log("-------------------------------------------------------- \n")
    save_in_log(f"                                                        \n")

# Función para abrir X fichero
def open_file (filepath):
    with open (filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Función para comprobar que un mensaje ha expirado de su tiempo
def expired_message (message_date):
    # Obtiene timestamp UTC actual
    today = datetime.datetime.utcnow()
    # Obtiene timestamp UTC del mensaje + diferencia de tiempo
    message_time = message_date + datetime.timedelta(minutes = DIFFERENCE_TIME)
    
    # Comprueba si ha pasado ya el tiempo
    if today > message_time:
        return True
    else:
        return False

# Función para guardar X texto en el log
def save_in_log (text):
    # Nombre del archivo a crear/escribir
    filename = f"{datetime.datetime.today().strftime('%d-%m-%Y')}.log"

    # Si el archivo ya ha sido creado
    if (os.path.isfile(filename)):
        # Abrir el archivo en modo añadir
        file = open(filename, 'a', encoding='utf-8')
    # Si el archivo no ha sido creado
    else:
        # Abrir el archivo en modo sustituir
        file = open(filename, 'w', encoding='utf-8')

    # Añade/Escribe el contenido
    file.write(text)
    # Cierra el fichero
    file.close();