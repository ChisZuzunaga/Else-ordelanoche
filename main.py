import keyboard
from playsound import playsound

# Archivo de audio
audio_file = 'noche.mp3'  # Cambia esto según el archivo

# Contador de pulsaciones
press_count = 0

def on_key_event(e):
    global press_count
    # Verifica si la tecla presionada es 'r'
    if e.name == 'r' and e.event_type == 'down':
        press_count += 1
        print(f'Botón presionado {press_count} veces')

        if press_count == 2:
            print("Reproduciendo audio...")
            playsound(audio_file)
            # Reinicia el contador
            press_count = 0

# Escucha el evento de la tecla 'r'
keyboard.hook(on_key_event)

print("Presiona la tecla 'r' dos veces para reproducir el audio. Presiona ESC para salir.")
keyboard.wait('esc')  # Espera hasta que se presione la tecla ESC
