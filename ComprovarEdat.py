"""
Samuel Antón
01/10/2025
ASIXc1B
MDS - TA02
"""
#!/usr/bin/env python3
import datetime

def demanar_enter(prompt):
    #Demana un número enter per consola i gestiona errors de conversió.
    while True:
        s = input(prompt).strip()
        if not s:
            print("No has escrit res. Torna-ho a provar.")
            continue
        try:
            return int(s)
        except ValueError:
            print("Si us plau, introdueix un número enter vàlid.")

def demanar_data_naixement():
    #Demana any, mes i dia per separat, valida i retorna un objecte datetime.date.
    avui = datetime.date.today()
    while True:
        print("\nIntrodueix la teva data de naixement:")
        any_naix = demanar_enter("  Any (ex. 2007): ")
        mes = demanar_enter("  Mes (1-12): ")
        dia = demanar_enter("  Dia (1-31): ")

        # Intentar construir la data (això valida dies segons el mes i any, incloent anys de traspàs)
        try:
            data = datetime.date(any_naix, mes, dia)
        except ValueError as e:
            print(f"Data invàlida, error del sistema: {e}. Torna-ho a provar.")
            continue

        # No acceptar dates en el futur
        if data > avui:
            print(f"La data {data.isoformat()} és en el futur (avui és {avui.isoformat()}). Torna-ho a provar.")
            continue

        # Tot correcte
        return data

def calcular_edat(data_naix, referencia=None):
    #Calcula l'edat en anys complets respecte a la data 'referencia' (per defecte avui).#
    if referencia is None:
        referencia = datetime.date.today()
    anys = referencia.year - data_naix.year
    # Si no ha complert anys aquest any, restar 1
    if (referencia.month, referencia.day) < (data_naix.month, data_naix.day):
        anys -= 1
    return anys

def main():
    avui = datetime.date.today()
    data_naix = demanar_data_naixement()
    edat = calcular_edat(data_naix, avui)

    print(f"\nData de naixement registrada: {data_naix.isoformat()}")
    print(f"Data d'avui: {avui.isoformat()}")
    print(f"Tens {edat} anys.")

    if edat >= 18:
        print("Ets major d'edat.")
    else:
        print("Ets menor d'edat.")

if __name__ == "__main__":
    main()