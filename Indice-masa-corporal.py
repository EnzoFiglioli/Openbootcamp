peso =  input ("Por favor indica tu peso (solo en numeros y sin comas ','): ")
altura = input ("Y ahora indicanos tu altura: ")
peso = float (peso)
altura = float (altura)
iMC = peso / (altura ** 2)

import decimal

iMC = decimal.Decimal(iMC)

redondeo = round (iMC, 3)

print (f"Tu índice de masa corporal es de {iMC}.")