import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import pandas as pd

# Configuración inicial de customtkinter
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "dark-blue", "green"

def seleccionar_archivo():
    """Abre un cuadro de diálogo para seleccionar un archivo y muestra el nombre del archivo seleccionado."""
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        etiqueta_archivo.configure(text=f"Archivo seleccionado: {archivo}")
    else:
        etiqueta_archivo.configure(text="No se ha seleccionado ningún archivo.")

def leer_archivo():
    """Funcion para leer el archivo"""
    pass  # Implementar en el futuro

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Selector de Archivos")
ventana.geometry("500x200")

# Crear frame para poner los botones dentro del frame
frame = ctk.CTkFrame(ventana, width=300, height=100, fg_color='transparent')
frame.pack(expand=True)

# Cargar la fuente personalizada
fuente_personalizada = ctk.CTkFont(family= 'Coolvetica', size= 20)

# Etiqueta para mostrar el archivo seleccionado
etiqueta_archivo = ctk.CTkLabel(
    frame, text="No se ha seleccionado ningún archivo.", wraplength=450, justify="left", font= fuente_personalizada
)
etiqueta_archivo.pack(pady=20)

# Cargar ícono de archivo
try:
    foto = Image.open('File_Icon.png')
    icono_imagen = ctk.CTkImage(light_image=foto, dark_image=foto, size=(44, 44))
except FileNotFoundError:
    print("Error: File_Icon.png no encontrado. El botón se mostrará sin imagen.")
    icono_imagen = None
    
try:
    foto2 = Image.open('Encrypt_Icon.png')
    encriptar_imagen = ctk.CTkImage(light_image= foto2, dark_image= foto2, size=(44,44))
except FileNotFoundError:
    print("Error: Encrypt_Icon.png no encontrado. El botón se mostrará sin imagen.")
    encriptar_imagen = None
    
# Botón para subir archivos
boton_subir = ctk.CTkButton(
    frame,
    text="Subir Archivo",
    corner_radius=38,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font= fuente_personalizada,
    image=icono_imagen,
    command=seleccionar_archivo
)
boton_subir.pack(padx=10, pady=10, side='left')

#Boton para leer los archivos
button = ctk.CTkButton(
    frame,
    text='Encriptar archivo',
    corner_radius=38,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font= fuente_personalizada,
    image= encriptar_imagen,
    command=leer_archivo)
button.pack(padx=10, pady=10, side='right')

# Ejecutar la aplicación
ventana.mainloop()
