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

# Ejemplo de uso
polinomio = "x^4+x^2+1"
binario, grado = polinomio_a_binario_y_grado(polinomio)

print(f"Cadena binaria: {binario}")
print(f"Grado del polinomio: {grado}")
def crc_remainder(input_bits, polynomial):
    # Agregar ceros al final de la entrada
    input_bits = input_bits + '0' * (len(polynomial) - 1)
    
    # Realizar la división
    input_length = len(input_bits)
    polynomial_length = len(polynomial)
    
    # Convertir cadenas a listas de enteros
    input_bits = [int(bit) for bit in input_bits]
    polynomial = [int(bit) for bit in polynomial]
    
    for i in range(input_length - polynomial_length + 1):
        if input_bits[i] == 1:  # Solo dividir si el primer bit es 1
            for j in range(polynomial_length):
                input_bits[i + j] ^= polynomial[j]  # XOR
    
    # El residuo es lo que queda
    return ''.join(str(bit) for bit in input_bits[-(polynomial_length - 1):])

# Ejemplo de uso
data = "1101"  # Datos originales
polynomial = "1011"  # Polinomio generador
crc = crc_remainder(data, polynomial)
print(f"CRC: {crc}")
