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

