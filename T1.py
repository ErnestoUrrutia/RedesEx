#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
#pulsos= [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0]
pulsos= []
print("Digitatu cadena de 0 y 1\n")
pulsos=[int(digito) for digito in input()]
fig, axs = plt.subplots(3, 1, figsize=(12, 8))
#******************************* NRZ-L ***********************************
j=0
nrzl=[]
etiquetasnrzl=[]
for i in pulsos:
    if i==0:
        nrzl.append(-1)
    else:
        nrzl.append(1)
    etiquetasnrzl.append(f"t({j})")
    j=j+1
if nrzl[-1]==1:
    nrzl.append(-1)
else:
    nrzl.append(1)
axs[0].step(np.arange(len(nrzl)) , nrzl, where='post', color='b', linewidth=2)
axs[0].set_title("NRZ-L")
axs[0].set_ylim(-1.5, 1.5)  
axs[0].grid(True, which='both', linestyle='-.', linewidth=0.5)
axs[0].set_xticks(np.arange(0, len(np.arange(len(etiquetasnrzl))), 1))
axs[0].set_xticklabels(etiquetasnrzl)
for i, valor in enumerate(pulsos):
    axs[0].text(i+0.5, 1.1, str(valor), ha='center', va='bottom', color='red', fontsize=16)
#******************************* Manchester ***********************************
manchester = []
etiquetasManchester=[]
j=1
for bit in pulsos:
    if bit == 1:#modificar a 0 si la configuracion de manchester es la contraria
        manchester.extend([1, 0])
    else:
        manchester.extend([0, 1])
for i in range(0,len(manchester)):
    if i%2!=0:
        etiquetasManchester.append(f"t({j})")
        j=j+1
    else:
        etiquetasManchester.append("")
if manchester[-1]==1:
    manchester.append(1)
else:
    manchester.append(0)
axs[1].step(np.arange(len(manchester)), manchester, where='post', color='r', linewidth=2)
axs[1].set_title("Manchester")
axs[1].set_ylim(-0.5, 1.5)
axs[1].grid(True, which='both', linestyle='-.', linewidth=0.5)
axs[1].set_xticks(np.arange(0, len(etiquetasManchester), 1))
axs[1].set_xticklabels(etiquetasManchester)
for i, valor in enumerate(pulsos):
    axs[1].text(i*2+1, 1.2, str(valor), ha='center', va='bottom', color='red', fontsize=16)
#******************************* 8B10B ***********************************

map_5b6b = {
    "00000": "111111",  
    "00001": "111110",
    "00010": "111101",
    "00011": "111100",
    "00100": "111011",
    "00101": "111010",
    "00110": "111001",
    "00111": "111000",
    "01000": "110111",
    "01001": "110110",
    "01010": "110101",
    "01011": "110100",
    "01100": "110011",
    "01101": "110010",
    "01110": "110001",
    "01111": "110000",
    "10000": "101111",
    "10001": "101110",
    "10010": "101101",
    "10011": "101100",
    "10100": "101011",
    "10101": "101010", 
    "10110": "101001",
    "10111": "101000",
    "11000": "100111",
    "11001": "100110",
    "11010": "100101",
    "11011": "100100",
    "11100": "100011",
    "11101": "100010",
    "11110": "100001",
    "11111": "100000",
}

map_3b4b = {
    "000": "0000",
    "001": "0001",
    "010": "0010",
    "011": "0011", 
    "100": "0100",
    "101": "0101",
    "110": "0110",
    "111": "0111",  
}

def encode_8b10b(input_bits):
    part_5b = input_bits[:5]
    part_3b = input_bits[5:]
    encoded_6b = map_5b6b.get(part_5b)
    encoded_4b = map_3b4b.get(part_3b)
    encoded_10b = encoded_6b + encoded_4b
    return encoded_10b
encoded_bits = encode_8b10b(''.join(str(bit) for bit in pulsos[:8]))
print(encoded_bits)
lista_enteros = [int(bit) for bit in encoded_bits]

j=0
cod8b10b=[]
etiquetascod8b10b=[]
for i in lista_enteros:
    if i==0:
        cod8b10b.append(0)
    else:
        cod8b10b.append(1)
    etiquetascod8b10b.append(f"t({j})")
    j=j+1

if cod8b10b[-1]==1:
    cod8b10b.append(1)
else:
    cod8b10b.append(0)
axs[2].step(np.arange(len(cod8b10b)) , cod8b10b, where='post', color='b', linewidth=2)
axs[2].set_title("8B10B")
axs[2].set_ylim(-0.5, 1.5)  
axs[2].grid(True, which='both', linestyle='-.', linewidth=0.5)
axs[2].set_xticks(np.arange(0, len(np.arange(len(etiquetascod8b10b))), 1))
axs[2].set_xticklabels(etiquetascod8b10b)
for i in range(10):
    axs[2].text(i+0.5, 1.1, str(cod8b10b[i]), ha='center', va='bottom', color='red', fontsize=16)
plt.tight_layout()
plt.show()
