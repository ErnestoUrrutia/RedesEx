import re

def polinomio_a_binario_y_grado(polinomio):
    # Encontrar los exponentes en el polinomio
    terminos = re.findall(r'x\^(\d+)|x|1', polinomio)
    
    # Extraer los grados de los términos
    grados = []
    for termino in terminos:
        if termino == '':        # Caso de x sin exponente (es x^1)
            grados.append(1)
        elif termino == '1':      # Caso del término independiente 1 (es x^0)
            grados.append(0)
        else:                     # Caso general (x^n)
            grados.append(int(termino))
    
    # Obtener el grado máximo
    grado = max(grados)
    
    # Crear la cadena binaria
    binario = ''.join('1' if i in grados else '0' for i in range(grado, -1, -1))
    
    return binario, grado

def crc_calculo(mensaje, polinomio):
    # Convierte el polinomio a binario y obtén su grado
    polinomio_binario, grado = polinomio_a_binario_y_grado(polinomio)
    
    # Agregar ceros al final del mensaje según el grado del polinomio
    mensaje += '0' * grado
    
    # Convertir a listas de enteros para manipulación
    mensaje = [int(bit) for bit in mensaje]
    polinomio = [int(bit) for bit in polinomio_binario]

    # Realizar la división binaria (XOR)
    for i in range(len(mensaje) - grado):
        if mensaje[i] == 1:  # Solo dividir si el bit actual es 1
            for j in range(len(polinomio)):
                mensaje[i + j] ^= polinomio[j]
    
    # El residuo es el CRC
    crc = ''.join(str(bit) for bit in mensaje[-grado:])
    return crc

# Ejemplo de uso
mensaje = "11010011101100"  # Datos de ejemplo
polinomio = "x^4 + x + 1"   # Polinomio de ejemplo para CRC

# Calcula el CRC
crc = crc_calculo(mensaje, polinomio)
print(f"Mensaje original: {mensaje}")
print(f"CRC calculado: {crc}")
print(f"Mensaje con CRC: {mensaje + crc}")
