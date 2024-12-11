import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

# Configuración inicial de customtkinter
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "dark-blue", "green"

def seleccionar_archivo():
    """Abre un cuadro de diálogo para seleccionar un archivo y muestra el nombre del archivo seleccionado."""
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        etiqueta_archivo.configure(text=f"Archivo seleccionado: {archivo}")
        return archivo
    else:
        etiqueta_archivo.configure(text="No se ha seleccionado ningún archivo.")

def encriptar_archivo():
    archivo = seleccionar_archivo()
    if archivo:
        print(f"Archivo a encriptar: {archivo}")

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Selector de Archivos")
ventana.geometry("500x200")

# Etiqueta para mostrar el archivo seleccionado
etiqueta_archivo = ctk.CTkLabel(
    ventana, text="No se ha seleccionado ningún archivo.", wraplength=450, justify="left"
)
etiqueta_archivo.pack(pady=20)

# Cargar ícono de archivo
try:
    foto = Image.open('File_Icon.png')
    icono_imagen = ctk.CTkImage(light_image=foto, dark_image=foto, size=(32, 32))
except FileNotFoundError:
    print("Error: File_Icon.png no encontrado. El botón se mostrará sin imagen.")
    icono_imagen = None

# Botón para subir archivos
boton_subir = ctk.CTkButton(
    ventana,
    text="Subir Archivo",
    corner_radius=38,
    fg_color='transparent',
    border_color='#FF5733',
    border_width=2,
    hover_color='#362522',
    image=icono_imagen,
    command=seleccionar_archivo
)
boton_subir.place(relx=0.5, rely=0.5, anchor='center')

# Ejecutar la aplicación
ventana.mainloop()
