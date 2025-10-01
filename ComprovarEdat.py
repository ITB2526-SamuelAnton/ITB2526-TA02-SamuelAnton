"""
Samuel Antón
01/10/2025
ASIXc1B
MDS - TA02
"""

from datetime import datetime

# Demanar edat
edat = int(input("Quina edat tens? "))

# Comprovar si és major d'edat
if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")

# Funcionalitat 1: Categoritzar edat
if edat < 13:
    print("Ets un infant")
elif edat < 18:
    print("Ets un adolescent")
elif edat <60:
    print("Ets una persona gran")
else:
    print("Ets un ancià")

# Funcionalitat 2: Calcular en quin any farà 100 anys
any_actual = datetime.now().year
any_100 = any_actual + (100 - edat)
print(f"Faràs 100 anys l'any {any_100}")

print("Programa Finalitzat")
