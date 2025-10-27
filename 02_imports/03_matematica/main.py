# BIBLIOTEca
import math

# entrada de dados 
r = float(input("informe o raio do circulo: ").strip().replace(",","."))

# calculo

a = math.pi*(r**2)
c = 2 *math.pi*r 

#saída de dados
print(f"número do pi: {math.pi}")
print(f"Área da circunferência: {a:.2f}")
print(f"tamanho a circunferencia: {c:.2f}")