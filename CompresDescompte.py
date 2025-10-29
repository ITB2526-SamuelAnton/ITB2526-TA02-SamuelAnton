# python
# python
import sys

try:
    preu_input = input("Introdueix el preu original del producte: ")
    try:
        preuOrginal = float(preu_input)
    except ValueError:
        print("Has d'introduir un número vàlid per al preu original.")
        sys.exit(1)
    if preuOrginal < 0:
        raise ValueError("El preu original no pot ser negatiu.")
    if preuOrginal == 0:
        raise ValueError("El preu original no pot ser zero.")
    percent_input = input("Introdueix el percentatge de descompte (sense el símbol %): ")
    try:
        percentatgeDescompte = float(percent_input)
    except ValueError:
        print("Has d'introduir un número vàlid per al percentatge de descompte.")
        sys.exit(1)
    if percentatgeDescompte == 0:
        raise ValueError("El percentatge de descompte no pot ser zero.")
    if percentatgeDescompte < 0:
        raise ValueError("El percentatge de descompte no pot ser negatiu.")
    if percentatgeDescompte > 100:
        raise ValueError("El percentatge de descompte no pot ser superior al 100\%.")
    descompte = (preuOrginal * percentatgeDescompte) / 100
    preuFinal = preuOrginal - descompte
    if preuFinal <= 0:
        raise ValueError("El preu final no pot ser negatiu. Revisa els valors introduïts.")
    print(f"El preu final després del descompte és: {preuFinal:.2f} unitats monetàries.")
except (EOFError, KeyboardInterrupt):
    print("\nEntrada interrompuda per l'usuari.")
    sys.exit(1)
except ValueError as ve:
    print(ve)
    sys.exit(1)
except Exception as e:
    print(f"S'ha produït un error inesperat: {e}")
    sys.exit(1)

#Aquest codi calcula el preu final d'un producte després d'aplicar un descompte.
# Demana a l'usuari el preu original i el percentatge de descompte, i mostra el preu final.
# Inclou gestió d'errors per assegurar que l'entrada de l'usuari és vàlida.
# Fi del codi CompresDescompte.py
