from bitstring import BitArray #instalada com pip
import itertools

def bin2int(a):
    b = BitArray(bin=a)
    return b.int

def int2bin(a, length):
    # para valores unsigned, usamos uint=a ao inves de int=a
    b = BitArray(int=a, length = length) # lenght eh o tamanho da string binaria
    return b.bin

BITS_ENTRADA = 4
BITS_SAIDA = 5

input_f = open("entradas.txt","w")
output_f = open("saidas_ref.txt","w")
testes_a = range(-8, 8)
testes_b = range(-8, 8)

for a,b in itertools.product(testes_a, testes_b):
    res = a + b #minha saida de referencia
    
    bin_a = int2bin(a, BITS_ENTRADA)
    bin_b = int2bin(b, BITS_ENTRADA)
    bin_res = int2bin(res, BITS_SAIDA)
    
    print(f'{bin_a} {bin_b}', file = input_f)
    print(bin_res, file = output_f)

input_f.close()
output_f.close()
