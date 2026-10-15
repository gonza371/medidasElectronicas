import serial
import time


PUERTO = '/dev/ttyUSB0'  
BAUD_RATE = 9600

# Saltos definidos en el procedimiento
frecuencias_barrido = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

try:
    gf = serial.Serial(PUERTO, BAUD_RATE, timeout=1)
    print(f"[*] Conectado al generador en {PUERTO}.")

    comandos_iniciales = [
        "SOUR:FUNC SIN\n",
        "SOUR:VOLT 5.0\n",
        "SOUR:VOLT:OFFS 0\n",
        "OUTP ON\n"
    ]
    
    for cmd in comandos_iniciales:
        gf.write(cmd.encode('ascii'))
        time.sleep(0.1)

    print("[*] Configuración inicial aplicada (Senoidal, 5Vpp, Offset 0V).")
    print("[*] Iniciando barrido con intervención del operador (Opción B).")


    for freq in frecuencias_barrido:

        input(f"\n[?] Presiona ENTER para ajustar la frecuencia a {freq} Hz...")
        
        comando_freq = f"SOUR:FREQ {freq}\n"
        gf.write(comando_freq.encode('ascii'))
        print(f" ---> Generando {freq} Hz. Observa el osciloscopio y toma nota.")

    print("\n[*] Barrido finalizado con éxito.")

except serial.SerialException as e:
    print(f"[!] Error de puerto serie: {e}")
finally:
    if 'gf' in locals() and gf.is_open:
        gf.close()