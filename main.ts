input.onButtonPressed(Button.A, function () {
    if (hours < 23) {
        hours += 1
    } else {
        hours = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    time = "" + hours + (":" + ("" + minutes) + "")
    basic.showString(time)
})
// CORREÇÃO DA LINHA 18: Agora aponta para a função correta
input.onButtonPressed(Button.AB, function () {
    ampm = !(ampm)
})
input.onButtonPressed(Button.B, function () {
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
    }
})
/**
 * --- Variáveis iniciais ---
 */
let ampm = false
let minutes = 0
let time = ""
let hours = 0
let adjust = 0
// --- CONFIGURAÇÃO DO ALARME ---
let alarme_hours = 15
let alarme_minutes = 8
basic.forever(function () {
    basic.pause(60000)
    // Espera 1 minuto
    // Atualiza o relógio
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
        if (hours < 23) {
            hours += 1
        } else {
            hours = 0
        }
    }
    // --- LÓGICA DO DESPERTADOR ---
    if (hours == alarme_hours && minutes == alarme_minutes) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
        // CORREÇÃO DA LINHA 58: Usando um ícone válido (ASLEEP lembra um despertador digital)
        basic.showIcon(IconNames.Happy)
    }
})
