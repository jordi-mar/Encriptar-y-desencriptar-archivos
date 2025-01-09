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
