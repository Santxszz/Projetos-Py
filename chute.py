import random
import os

os.system("cls")

dado = random.randint(0, 100)
tentativas = 0

while True:
    chute = int(input("Chute um número: "))
    
    if chute > dado:
        tentativas += 1
        print("Você errou! O número é menor que {}".format(chute))
    
    if chute < dado: 
        tentativas += 1
        print("Você errou! O número é maior que {}".format(chute))
    
    if chute == dado:
        tentativas += 1
        print("Você acertou! O número era: {}".format(dado))
        print("Você usou {} tentativas".format(tentativas))
    