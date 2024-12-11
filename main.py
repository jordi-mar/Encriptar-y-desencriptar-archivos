import customtkinter as ctk
from tkinter import filedialog

# Configuración inicial de customtkinter
ctk.set_appearance_mode("System")  # Modo de apariencia: "System", "Dark" o "Light"
ctk.set_default_color_theme("blue")  # Tema de color: "blue", "dark-blue", "green"

def seleccionar_archivo():
    """Abre un cuadro de diálogo para seleccionar un archivo y muestra el nombre del archivo seleccionado."""
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        etiqueta_archivo.configure(text=f"Archivo seleccionado: {archivo}")
    else:
        etiqueta_archivo.configure(text="No se ha seleccionado ningún archivo.")

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Selector de Archivos")
ventana.geometry("500x200")

# Etiqueta para mostrar el archivo seleccionado
etiqueta_archivo = ctk.CTkLabel(ventana, text="No se ha seleccionado ningún archivo.", wraplength=450, justify="left")
etiqueta_archivo.pack(pady=20)

# Botón para subir archivos
boton_subir = ctk.CTkButton(ventana, text="Subir Archivo", command=seleccionar_archivo)
boton_subir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
