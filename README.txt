Crear venv con "esptool"

Para generar el .exe: "pyinstaller --onefile --name "UpdateFwESP" flash_fw.py"

"pip install pyserial"
"pip install esptool"

---------------------------------------------------------------------------

Para actualizar el firmware de la ESP32:

1. Conecta la ESP32 a tu computadora.

2. Abre una terminal o línea de comandos.

3. Ejecuta el siguiente comando:

   "python flash_fw.py"

El script detectará automáticamente el puerto y actualizará el firmware.


