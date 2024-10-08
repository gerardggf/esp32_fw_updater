import os
import sys
import subprocess
from tkinter import filedialog
import serial.tools.list_ports
import tkinter as tk
import time

def seleccionar_archivo():
    # Crea una ventana oculta para el diálogo de selección
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abre el diálogo para seleccionar un archivo
    archivo_seleccionado = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Todos los archivos", "*.*")]  # Puedes especificar otros tipos de archivos si lo deseas
    )

    # Devuelve la ruta del archivo seleccionado
    return archivo_seleccionado


# No lo utilizamos por ahora
# def find_bin_file(directory):
#     for file in os.listdir(directory):
#         if file.endswith('.bin'):
#             return os.path.join(directory,file)
#     return None

def detect_port_esp32():
    puertos = serial.tools.list_ports.comports()
    for puerto in puertos:
        if 'USB' in puerto.description or 'UART' in puerto.description:
            return puerto.device
    return None

def flash_firmware():
    try:
         # Detecta automáticamente el puerto donde está conectada la ESP32
        port = detect_port_esp32()
        if not port:
            print("No se pudo detectar el puerto de la ESP32.")
            return

        print(f"Puerto detectado: {port}")

        print('Selecciona el archivo del firmware para cargar (.bin)')
        firmware_path = seleccionar_archivo()
        print(firmware_path)

        if not os.path.exists(firmware_path):
            print("El archivo de firmware no existe en la carpeta actual.")
            return

        # Comando para flashear el firmware
        command = ['python','-m','esptool', '--chip', 'esp32', '--port', port, 'write_flash', '-z', '0x1000', firmware_path
        ]
        subprocess.run(command, check=True)

        # Esperamos un segundo por si las moscas
        time.sleep(1)

         # Comando para reiniciar la ESP32
        command2 = ['python', '-m', 'esptool', '--chip', 'esp32', '--port', port, 'run']
        subprocess.run(command2, check=True)

        print("Firmware actualizado correctamente.")
        print("Ya puedes cerrar la ventana")
    except Exception as e:
        print(f"Error al flashear el firmware: {e}")
        input()



if __name__ == '__main__':
    flash_firmware()
