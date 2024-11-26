import random
print("Chiedi Carta: 1, Stai: 2")
numero1 = random.randint(0,10)
print(numero1)
while(True):
 numero2 = random.randint(0,10)
 carta = int(input())
 numero3 = numero1+numero2
 if(carta==1):
    print(numero2)
    print("Hai", numero3)
 else:print("Hai", numero1)
 break
if(carta==2):
   print("Hai", numero3)


