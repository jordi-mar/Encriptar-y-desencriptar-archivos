import os
import base64
from cryptography.fernet import Fernet
from tkinter import filedialog, messagebox

def generate_key():
    key = Fernet.generate_key()
    key_path = filedialog.asksaveasfilename(title="Guardar archivo de la key", defaultextension=".key",
                                            filetypes=[("Key Files", "*.key")])
    if key_path:
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key, os.path.basename(key_path)
    else:
        return None, None

def load_key():
    key_path = filedialog.askopenfilename(title="Select Key File",
                                          filetypes=[("Key Files", "*.key")])
    if key_path and os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        return key, os.path.basename(key_path)
    else:
        messagebox.showerror("Key Missing",
                             "No se ha encontrado un archivo de key válido. Genera o selecciona otra key.")
        return None, None

def encrypt_file(selected_file, key):
    if not selected_file:
        messagebox.showerror("Error", "No se ha seleccionado un archivo para encriptar.")
        return

    if not key:
        messagebox.showerror("Error", "No se ha cargado la key. Por favor carga o genera una key primero.")
        return

    try:
        with open(selected_file, "rb") as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        # Convertir los datos encriptados a base64 para que sea legible como texto
        encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')

        # Sobrescribir el archivo original con los datos encriptados (en base64)
        with open(selected_file, "w") as file:
            file.write(encrypted_base64)

        messagebox.showinfo("Éxito", f"Archivo encriptado correctamente: {selected_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

def decrypt_file(selected_file, key):
    if not selected_file:
        messagebox.showerror("Error", "No se ha seleccionado un archivo para desencriptar.")
        return

    if not key:
        messagebox.showerror("Error", "Key no cargada. Por favor carga o genera una key primero.")
        return

    try:
        with open(selected_file, "r") as file:
            encrypted_base64 = file.read()

        # Convertir el texto base64 de nuevo a datos binarios
        encrypted_data = base64.b64decode(encrypted_base64)

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        # Sobrescribir el archivo original con los datos desencriptados
        with open(selected_file, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Éxito", f"Archivo desencriptado correctamente: {selected_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
