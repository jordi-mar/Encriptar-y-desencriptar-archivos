from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

def encriptar_archivo(ruta_archivo, clave, archivo_salida):
    """
    Encripta un archivo con una clave usando AES en modo CBC.
    
    Parámetros:
        ruta_archivo (str): Ruta del archivo a encriptar.
        clave (str): Clave para la encriptación.
        archivo_salida (str): Ruta del archivo encriptado de salida.
    """
    # Derivar una clave de 32 bytes a partir de la clave proporcionada
    backend = default_backend()
    salt = os.urandom(16)  # Sal aleatoria para mayor seguridad
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(clave.encode('utf-8'))
    
    # Generar un vector de inicialización (IV) aleatorio
    iv = os.urandom(16)
    
    # Crear el cifrador AES en modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    
    # Leer los datos del archivo y aplicar padding
    with open(ruta_archivo, 'rb') as f:
        datos = f.read()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    datos_padded = padder.update(datos) + padder.finalize()
    
    # Encriptar los datos
    datos_encriptados = encryptor.update(datos_padded) + encryptor.finalize()
    
    # Guardar el archivo encriptado con el salt y el IV
    with open(archivo_salida, 'wb') as f:
        f.write(salt + iv + datos_encriptados)
    
    print(f"Archivo encriptado guardado en: {archivo_salida}")

# Ejemplo de uso
ruta = "archivo.txt"  # Ruta del archivo a encriptar
clave = "mi_clave_segura"  # Clave para la encriptación (puedes personalizarla)
archivo_salida = "archivo_encriptado.bin"  # Archivo de salida
encriptar_archivo(ruta, clave, archivo_salida)
