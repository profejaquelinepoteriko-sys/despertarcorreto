def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
    else:
        hours = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global time
    time = "" + str(hours) + (":" + ("" + str(minutes)) + "")
    basic.show_string(time)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# CORREÇÃO DA LINHA 18: Agora aponta para a função correta

def on_button_pressed_ab():
    global ampm
    ampm = not (ampm)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

"""

--- Variáveis iniciais ---

"""
ampm = False
minutes = 0
time = ""
hours = 0
adjust = 0
# --- CONFIGURAÇÃO DO ALARME ---
alarme_hours = 7
alarme_minutes = 41

def on_forever():
    global minutes, hours
    basic.pause(60000)
    # Espera 1 minuto
    # Atualiza o relógio
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
        if hours < 23:
            hours += 1
        else:
            hours = 0
    # --- LÓGICA DO DESPERTADOR ---
    if hours == alarme_hours and minutes == alarme_minutes:
        music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
            music.PlaybackMode.IN_BACKGROUND)
        # CORREÇÃO DA LINHA 58: Usando um ícone válido (ASLEEP lembra um despertador digital)
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
