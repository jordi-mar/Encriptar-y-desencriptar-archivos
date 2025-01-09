import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64  # Para convertir los datos binarios en texto legible
from PIL import Image

# Configuración inicial de customtkinter
ctk.set_appearance_mode("Dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "dark-blue", "green"

class FileEncryptorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure File Encrypter/Decrypter")
        self.master.geometry("700x450")

        self.key = None

        # Cargar la fuente personalizada
        self.fuente_personalizada = ctk.CTkFont(family='Coolvetica', size=25)

        # Crear frame principal
        self.frame = ctk.CTkFrame(master, width=300, height=100, fg_color='transparent')
        self.frame.pack(expand=True)

        # Etiqueta para mostrar el archivo seleccionado
        self.etiqueta_archivo = ctk.CTkLabel(
            self.frame, text="No se ha seleccionado ningún archivo.", wraplength=700, justify="left", font=self.fuente_personalizada
        )
        self.etiqueta_archivo.pack(pady=20)

        # Cargar íconos
        try:
            foto = Image.open('File_Icon.png')
            self.icono_imagen = ctk.CTkImage(light_image=foto, dark_image=foto, size=(44, 44))
        except FileNotFoundError:
            print("Error: File_Icon.png no encontrado. El botón se mostrará sin imagen.")
            self.icono_imagen = None

        try:
            foto2 = Image.open('Encrypt_Icon.png')
            self.encriptar_imagen = ctk.CTkImage(light_image=foto2, dark_image=foto2, size=(44, 44))
        except FileNotFoundError:
            print("Error: Encrypt_Icon.png no encontrado. El botón se mostrará sin imagen.")
            self.encriptar_imagen = None

        try:
            foto3 = Image.open('Key_Icon.png')
            self.key_imagen = ctk.CTkImage(light_image=foto3, dark_image=foto3, size=(44, 44))
        except FileNotFoundError:
            print("Error: Key_Icon.png no encontrado. El botón se mostrará sin imagen.")
            self.key_imagen = None

        # Botón para subir archivos
        self.boton_subir = ctk.CTkButton(
            self.frame,
            text="Subir Archivo",
            corner_radius=38,
            fg_color='transparent',
            border_color='#FF5733',
            border_width=2,
            hover_color='#362522',
            font=self.fuente_personalizada,
            image=self.icono_imagen,
            command=self.seleccionar_archivo
        )
        self.boton_subir.pack(padx=10, pady=10, side='top')

        # Botón para encriptar archivos
        self.boton_encriptar = ctk.CTkButton(
            self.frame,
            text='Encriptar Archivo',
            corner_radius=38,
            fg_color='transparent',
            border_color='#FF5733',
            border_width=2,
            hover_color='#362522',
            font=self.fuente_personalizada,
            image=self.encriptar_imagen,
            command=self.encrypt_file
        )
        self.boton_encriptar.pack(padx=10, pady=10, side='top')

        # Botón para desencriptar archivos
        self.boton_desencriptar = ctk.CTkButton(
            self.frame,
            text='Desencriptar Archivo',
            corner_radius=38,
            fg_color='transparent',
            border_color='#FF5733',
            border_width=2,
            hover_color='#362522',
            font=self.fuente_personalizada,
            image=self.encriptar_imagen,
            command=self.decrypt_file
        )
        self.boton_desencriptar.pack(padx=10, pady=10, side='top')

        # Botón para cargar una key
        self.boton_cargar_key = ctk.CTkButton(
            self.frame,
            text='Cargar Key',
            corner_radius=38,
            fg_color='transparent',
            border_color='#FF5733',
            border_width=2,
            hover_color='#362522',
            font=self.fuente_personalizada,
            image=self.key_imagen,
            command=self.load_key
        )
        self.boton_cargar_key.pack(padx=10, pady=10, side='top')

        # Botón para generar una nueva key
        self.boton_generar_key = ctk.CTkButton(
            self.frame,
            text='Generar Key',
            corner_radius=38,
            fg_color='transparent',
            border_color='#FF5733',
            border_width=2,
            hover_color='#362522',
            font=self.fuente_personalizada,
            image=self.key_imagen,
            command=self.generate_key
        )
        self.boton_generar_key.pack(padx=10, pady=10, side='top')

    def seleccionar_archivo(self):
        """Abre un cuadro de diálogo para seleccionar un archivo y muestra el nombre del archivo seleccionado."""
        archivo = filedialog.askopenfilename(title="Seleccionar archivo")
        if archivo:
            self.selected_file = archivo
            self.etiqueta_archivo.configure(text=f"Archivo seleccionado: {archivo}")
        else:
            self.etiqueta_archivo.configure(text="No se ha seleccionado ningún archivo.")

    def generate_key(self):
        key = Fernet.generate_key()
        key_path = filedialog.asksaveasfilename(title="Guardar archivo de la key", defaultextension=".key",
                                                filetypes=[("Key Files", "*.key")])
        if key_path:
            with open(key_path, "wb") as key_file:
                key_file.write(key)
            messagebox.showinfo("Se ha generado la Key", f"Una nueva key ha sido guardada como {key_path}")

    def load_key(self):
        key_path = filedialog.askopenfilename(title="Select Key File",
                                              filetypes=[("Key Files", "*.key")])
        if key_path and os.path.exists(key_path):
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            messagebox.showinfo("Key cargada", f"Key cargada correctamente desde {key_path}")
        else:
            messagebox.showerror("Key Missing",
                                 "No se ha encontrado un archivo de key válido. Genera o selecciona otra key.")

    def encrypt_file(self):
        if not hasattr(self, 'selected_file') or not self.selected_file:
            messagebox.showerror("Error", "No se ha seleccionado un archivo para encriptar.")
            return

        if not self.key:
            messagebox.showerror("Error", "No se ha cargado la key. Por favor carga o genera una key primero.")
            return

        try:
            with open(self.selected_file, "rb") as file:
                data = file.read()

            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data)

            # Convertir los datos encriptados a base64 para que sea legible como texto
            encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')

            # Sobrescribir el archivo original con los datos encriptados (en base64)
            with open(self.selected_file, "w") as file:
                file.write(encrypted_base64)

            messagebox.showinfo("Éxito", f"Archivo encriptado correctamente: {self.selected_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def decrypt_file(self):
        if not hasattr(self, 'selected_file') or not self.selected_file:
            messagebox.showerror("Error", "No se ha seleccionado un archivo para desencriptar.")
            return

        if not self.key:
            messagebox.showerror("Error", "Key no cargada. Por favor carga o genera una key primero.")
            return

        try:
            with open(self.selected_file, "r") as file:
                encrypted_base64 = file.read()

            # Convertir el texto base64 de nuevo a datos binarios
            encrypted_data = base64.b64decode(encrypted_base64)

            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)

            # Sobrescribir el archivo original con los datos desencriptados
            with open(self.selected_file, "wb") as file:
                file.write(decrypted_data)

            messagebox.showinfo("Éxito", f"Archivo desencriptado correctamente: {self.selected_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = FileEncryptorApp(root)
    root.mainloop()