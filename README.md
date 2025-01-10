<h1 align="center">Encriptador y desencriptador de archivos </h1>

> [!IMPORTANT]
> Para que el código se muestre correctamente, hay que descargar también los archivos de los iconos (Encrypt_Icon, File_Icon, Key_Icon) y descargar la fuente (Coolvetica Rg). Para instalar la fuente hay que seleccionarla, darle click derecho y darle a instalar. **Estos elementos no son imprescindibles para el funcionamiento del código, únicamente afectan a su estética.**
>
### Descripción ###
Esta aplicación permite a los usuarios encriptar y desencriptar todo tipo de archivos de manera sencilla utilizando claves generadas por el sistema. Es ideal para proteger información sensible de accesos no autorizados. Hay que tener en cuenta que se encripta de manera simétrica, es decir, hay que usar la misma llave para encriptar que para desencriptar.
 
 ### Dependencias ###
Este programa hace uso de: customtkinter, cryptography, PIL, base64, os, tkinter.

Para instalar las dependencias necesarias hay que poner este comando en la terminal:
```
pip install customtkinter pillow cryptography
```

### Funcionamiento del codigo ###
En el archivo  _**main.py**_ es donde se encuentra la interfaz del usuario, hecha con customtkinter. Por otro lado, _**encriptar.py**_ contiene las funciones necesarias para el encriptamiento. El orden a seguir para encriptar un archivo es el siguiente:
1. **Subir archivo:** Seleccione un archivo para encriptar o desencriptar.
2. **Crear/Cargar llave:** Genere una nueva llave y guárdela en un archivo o carga una que ya hayas generado previamente.
3. **Encriptar archivo:** Encripte el archivo seleccionado utilizando la llave cargada.
4. **Desencriptar archivo:** Desencripte el archivo seleccionado utilizando la llave cargada.
