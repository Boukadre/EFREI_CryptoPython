from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') 

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)


@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        valeur_bytes = valeur.encode()  # str -> bytes
        decrypted = f.decrypt(valeur_bytes)  # Décryptage
        return f"Valeur décryptée : {decrypted.decode()}"  # bytes -> str
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"


@app.route('/encrypt/<key>/<valeur>')
def encrypt_with_key(key, valeur):
    try:
        f_user = Fernet(key.encode())  # Création d'un objet Fernet avec la clé utilisateur
        token = f_user.encrypt(valeur.encode())  # Chiffrement
        return f"Valeur encryptée avec clé personnalisée : {token.decode()}"
    except Exception as e:
        return f"Erreur lors de l'encryptage : {str(e)}"

@app.route('/decrypt/<key>/<valeur>')
def decrypt_with_key(key, valeur):
    try:
        f_user = Fernet(key.encode())  # Création d'un objet Fernet avec la clé utilisateur
        decrypted = f_user.decrypt(valeur.encode())  # Déchiffrement
        return f"Valeur décryptée avec clé personnalisée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"
