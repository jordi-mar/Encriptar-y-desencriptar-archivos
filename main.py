import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import encriptar as en
import os

# Configuración inicial de customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

archivo = None
llave = None

# Funciones para manejar eventos
def seleccionar_archivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        etiqueta_archivo.configure(text=f"Archivo seleccionado: {archivo}")
    else:
        etiqueta_archivo.configure(text="No se ha seleccionado ningún archivo.")

def encriptar():
    if not archivo:
        messagebox.showwarning("Archivo Missing", "No se ha seleccionado un archivo para desencriptar.")
    elif not llave:
        messagebox.showwarning("Key Missing", "No se ha encontrado una llave válida. Genera o selecciona una llave.")
    else:
        try:
            en.encrypt_file(archivo, llave)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al encriptar el archivo: {e}")

def desencriptar():
    if not archivo:
        messagebox.showwarning("Archivo Missing", "No se ha seleccionado un archivo para desencriptar.")
    elif not llave:
        messagebox.showwarning("Key Missing", "No se ha encontrado una llave válida. Genera o selecciona una llave.")
    else:
        try:
            en.decrypt_file(archivo, llave)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al desencriptar el archivo: {e}")

def generar_llave():
    global llave
    llave, llave_nombre = en.generate_key()
    etiqueta_key.configure(text=f"Llave seleccionada: {llave_nombre}")

def cargar_llave():
    global llave
    llave, llave_nombre = en.load_key()
    etiqueta_key.configure(text=f"Llave seleccionada: {llave_nombre}")

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Selector de Archivos")
ventana.geometry("1000x600")

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

# Etiqueta para mostrar la key
etiqueta_key = ctk.CTkLabel(
    frame, text="No se ha seleccionado ninguna llave.", wraplength=600, justify="left", font=fuente_personalizada
)
etiqueta_key.pack(pady=10)

# Cargar imágenes
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
    command=encriptar
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
    command=desencriptar
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
    command=generar_llave
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
    command=cargar_llave
)
boton_cargar.pack(padx=10, pady=5, side='left')

# Iniciar la aplicación
ventana.mainloop()
