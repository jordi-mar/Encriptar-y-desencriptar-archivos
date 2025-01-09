import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

# Configuración inicial de customtkinter
ctk.set_appearance_mode("Dark")  # "System", "Dark", "Light"
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
ventana.geometry("1000x400")

# Crear frame principal
frame = ctk.CTkFrame(ventana, width=500, height=400, fg_color='transparent')
frame.pack(expand=True)

# Cargar la fuente personalizada
fuente_personalizada = ctk.CTkFont(family='Coolvetica', size=35)

# Etiqueta para mostrar el archivo seleccionado
etiqueta_archivo = ctk.CTkLabel(
    frame, text="No se ha seleccionado ningún archivo.", wraplength=600, justify="left", font=fuente_personalizada
)
etiqueta_archivo.pack(pady=10)

# Cargar imagenes
try:
    foto = Image.open('File_Icon.png')
    icono_imagen = ctk.CTkImage(dark_image=foto, size=(44, 44))
    foto2 = Image.open('Encrypt_Icon.png')
    encriptar_imagen = ctk.CTkImage(dark_image=foto2, size=(44, 44))
    foto3 = Image.open('Key_Icon.png')
    llave_imagen = ctk.CTkImage(dark_image=foto3, size=(44, 44))
except FileNotFoundError:
    print("Error: Algún icono no se encontró. Los botones se mostrarán sin icono.")
    icono_imagen = None
    encriptar_imagen = None
    llave_imagen = None

# Crear subframes para organizar botones en filas
frame_fila1 = ctk.CTkFrame(frame, fg_color='transparent')
frame_fila1.pack(pady=10)

frame_fila2 = ctk.CTkFrame(frame, fg_color='transparent')
frame_fila2.pack(pady=10)

frame_fila3 = ctk.CTkFrame(frame, fg_color='transparent')
frame_fila3.pack(pady=10)

# Botón para subir archivos
boton_subir = ctk.CTkButton(
    frame_fila1,
    text="Subir Archivo",
    corner_radius=40,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font=fuente_personalizada,
    image=icono_imagen,
    command=seleccionar_archivo
)
boton_subir.pack(padx=10, pady=5, side='left')

# Botón para encriptar archivo
boton_encriptar = ctk.CTkButton(
    frame_fila2,
    text="Encriptar Archivo",
    corner_radius=40,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font=fuente_personalizada,
    image=encriptar_imagen,
    command=leer_archivo
)
boton_encriptar.pack(padx=10, pady=5, side='left')

# Botón para desencriptar archivo
boton_desencriptar = ctk.CTkButton(
    frame_fila2,
    text="Desencriptar Archivo",
    corner_radius=40,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font=fuente_personalizada,
    image=encriptar_imagen,
    command=leer_archivo
)
boton_desencriptar.pack(padx=10, pady=5, side='left')

# Botón para crear una llave
boton_crear = ctk.CTkButton(
    frame_fila3,
    text="Crear Llave",
    corner_radius=40,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font=fuente_personalizada,
    image=llave_imagen,
    command=leer_archivo
)
boton_crear.pack(padx=10, pady=5, side='left')

# Botón para cargar una llave
boton_cargar = ctk.CTkButton(
    frame_fila3,
    text="Cargar Llave",
    corner_radius=40,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    font=fuente_personalizada,
    image=llave_imagen,
    command=leer_archivo
)
boton_cargar.pack(padx=10, pady=5, side='left')

# Iniciar la aplicación
ventana.mainloop()
