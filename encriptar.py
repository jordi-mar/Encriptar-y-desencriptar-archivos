import os
from tkinter import Tk, filedialog, Button, Label, Entry, messagebox
from cryptography.fernet import Fernet

class File_Encryptor_App:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure File Encrypter/Decrypter")
        self.master.geometry("500x300")

        self.key = None

        # Etiqueta de encabezado
        self.label =Label(master, text = "Bienvenido al encriptador de archivos")
        self.label.pack(pady = 10)

        # Archivo de la key
        self.key_label = Label(master, text = "Path para el archivo de la key (opcional): ") 
        self.key_label.pack(pady = 5)

        self.key_entry = Entry(master, width = 40)
        self.key_entry.pack(pady = 5)

        self.load_key_btn = Button (master, text = "Cargar key", command = self.load_key)
        self.load_key_btn.pack(pady = 5)

        self.generate_key_btn = Button(master, text = "Generar una nueva key", command = self.generate_key)
        self.generate_key_btn.pack(pady = 5)

        # Botones
        self.encrypt_btn = Button(master, text = "Encriptar archivo", command = self.encrypt_file, width = 20)
        self.encrypt_btn.pack(pady = 10)

        self.decrypt_btn = Button(master, text = "Desencriptar archivos", command = self.decrypt_file, width = 20)
        self.decrypt_btn.pack(pady = 10)

    def generate_key(self):
        key = Fernet.generate_key()
        key_path = filedialog.asksaveasfilename (title = "Guardar archivo de la key", defaultextension = ".key", filetypes = [("Key Files","*.key")])
        if key_path:
            with open(key_path, "wb") as key_file:
                key_file.write(key)
            messagebox.showinfo("Se ha generado la Key", f"Una nueva key ha sido guardada como {key_path}")
    
    def load_key(self):
        key_path = self.key_entry.get() or filedialog.askopenfilename(title = "Select Key File", filetypes = [("Key Files", "*.key")])
        if key_path and os.path.exists(key_path):
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            messagebox.showinfo("Key cargada", f"Key cargada correctamente desde {key_path}")
        else:
            messagebox.showerror("Key Missing", "No se ha encontrado un archivo de key valido. Genera o selecciona otra key.")

    def encrypt_file(self):
        if not self.key:
            messagebox.showerror("Error", "No se ha cargado la key. Porfavor carga o genera una key primero.")
            return

        file_path = filedialog.askopenfilename(title = "Selecciona el archivo que desees encriptar")
        if not file_path:
            return

        try:
            with open(file_path, "rb") as file:
                data = file.read()

            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data)

            save_path = filedialog.asksaveasfilename(title = "Guardar archivo encriptado", defaultextension = ".enc", filetypes = [("Encrypted Files", "*.enc")])
            if save_path:
                with open(save_path, "wb") as file:
                    file.write(encrypted_data)

                messagebox.showinfo("Éxito", f"Archivo encriptado correctamente y guardado en {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def decrypt_file(self):
        if not self.key:
            messagebox.showerror("Error", "Key no cargada. Porfavor carga o genera una key primero.")
            return

        file_path = filedialog.askopenfilename(title = "Selecciona el archivo que desees desencriptar", filetypes = [("Encrypted Files", "*.enc")])
        if not file_path:
            return

        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)

            save_path = filedialog.asksaveasfilename(title = "Guardar archvio desencriptado", defaultextension ="", filetypes = [("All Files", "*.*")])
            if save_path:
                with open(save_path, "wb") as file:
                    file.write(decrypted_data)

                messagebox.showinfo("Éxito", f"Archivo desencriptado correctamente y guardado en {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    root = Tk()
    app = File_Encryptor_App(root)
    root.mainloop()