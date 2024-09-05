import os
import sys
import subprocess
import serial.tools.list_ports

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

        # Ruta del archivo de firmware
        firmware_path = os.path.join(os.getcwd(), 'firmware.bin')

        if not os.path.exists(firmware_path):
            print("El archivo de firmware no existe en la carpeta actual.")
            return

        # Comando para flashear el firmware
        command = [
            'esptool.py', '--chip', 'esp32', '--port', port, 'write_flash', '-z', '0x1000', firmware_path
        ]

        # Ejecutar el comando de flasheo
        subprocess.run(command, check=True)

        print("Firmware actualizado correctamente.")
    except Exception as e:
        print(f"Error al flashear el firmware: {e}")



if __name__ == '__main__':
    flash_firmware()
