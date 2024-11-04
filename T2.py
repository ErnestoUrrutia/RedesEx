import re

def polinomio_a_binario_y_grado(polinomio):
    terminos = re.findall(r'x\^(\d+)|x|1', polinomio)
    grados = []
    for termino in terminos:
        if termino == '':      
            grados.append(1)
        elif termino == '1': 
            grados.append(0)
        else:       
            grados.append(int(termino))
    grado = max(grados)
    binario = ''.join('1' if i in grados else '0' for i in range(grado, -1, -1))
    return binario, grado

def crc_calculo(mensaje, polinomio):
    polinomio_binario, grado = polinomio_a_binario_y_grado(polinomio)
    mensaje += '0' * grado
    mensaje = [int(bit) for bit in mensaje]
    polinomio = [int(bit) for bit in polinomio_binario]

    for i in range(len(mensaje) - grado):
        if mensaje[i] == 1:  
            for j in range(len(polinomio)):
                mensaje[i + j] ^= polinomio[j]
    
    crc = ''.join(str(bit) for bit in mensaje[-grado:])
    return crc





def crc_verificar(codeword, polinomio):
    polinomio_binario, grado = polinomio_a_binario_y_grado(polinomio)
    mensaje = [int(bit) for bit in codeword]
    polinomio = [int(bit) for bit in polinomio_binario]
    for i in range(len(mensaje) - grado):
        if mensaje[i] == 1:
            for j in range(len(polinomio)):
                mensaje[i + j] ^= polinomio[j]
    residuo = mensaje[-grado:]
    crc_valido = all(bit == 0 for bit in residuo)
    
    return crc_valido, ''.join(str(bit) for bit in residuo)


opc=int(input("Escoja la opcion:\n1.-Codificar\n2.-Decodificar"))
if opc==1:
    mensaje=input("Digite la cadena")
    polinomio=input("Digite el polinomio")
    #mensaje = "11010011101100"  # Datos de ejemplo
    #polinomio = "x^4 + x + 1"   # Polinomio de ejemplo para CRC
    # Calcula el CRC
    crc = crc_calculo(mensaje, polinomio)
    print(f"Mensaje original: {mensaje}")
    print(f"CRC calculado: {crc}")
    print(f"Mensaje con CRC: {mensaje + crc}")
elif opc==2:
    codeword=input("Digite la cadena encriptada")
    polinomio=input("Digite el polinomio")
    #codeword = "110100111011000110"  # Codeword de ejemplo (mensaje + CRC)
    #polinomio = "x^4 + x + 1"       # Polinomio para verificar el CRC
    # Verificar el CRC del codeword
    crc_valido, residuo = crc_verificar(codeword, polinomio)
    print(f"Codeword: {codeword}")
    print(f"Residuo: {residuo}")
    print("CRC válido" if crc_valido else "CRC inválido")
