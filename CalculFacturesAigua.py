# python
import re

def calcular_factura(consumo_litres):
    # Calcula la factura segons els litres consumits i retorna (total, operacio_text)
    quota_fixa = 6.0

    if consumo_litres < 0:
        raise ValueError("El consum no pot ser negatiu.")

    if consumo_litres < 50:
        tarifa = 0.0
        variable = 0.0
    elif consumo_litres <= 200:
        tarifa = 0.1
        variable = consumo_litres * tarifa
    else:
        tarifa = 0.3
        variable = consumo_litres * tarifa

    total = quota_fixa + variable
    operacio = (
        f"{quota_fixa:.2f} + {consumo_litres:.2f} * {tarifa:.2f} = "
        f"{quota_fixa:.2f} + {variable:.2f} = {total:.2f} €"
    )
    return total, operacio

def words_to_number(text):
    # Suport bàsic per convertir paraules a nombres (català / espanyol / anglès comunes)
    units = {
        "zero":0, "cero":0,
        "un":1, "una":1, "uno":1,
        "dos":2, "tres":3, "quatre":4, "cuatro":4, "cinco":5, "cinc":5,
        "sis":6, "seis":6, "set":7, "siete":7, "vuit":8, "ocho":8, "nou":9, "nueve":9,
        "deu":10, "diez":10, "ten":10
    }
    teens = {
        "once":11, "dotze":12, "doce":12, "tretze":13, "trece":13,
        "catorze":14, "catorce":14, "quinze":15, "quince":15,
        "setze":16, "dieciseis":16, "dieciséis":16, "disset":17, "diecisiete":17,
        "divuit":18, "dieciocho":18, "dinou":19, "diecinueve":19
    }
    tens = {
        "vint":20, "veinte":20, "trenta":30, "treinta":30,
        "quaranta":40, "cuarenta":40, "cinquanta":50, "cincuenta":50,
        "seixanta":60, "sesenta":60, "setanta":70, "setenta":70,
        "vuitanta":80, "ochenta":80, "noranta":90, "noventa":90,
        "eighty":80, "ninety":90, "forty":40, "thirty":30, "twenty":20
    }
    hundreds = {"cent":100, "cien":100, "ciento":100, "cento":100, "dos-cents":200, "doscents":200, "doscientos":200}

    # Normalitza i separa tokens (es descarten paraules comunes no numèriques)
    s = re.sub(r'[-,]', ' ', text.lower())
    tokens = [t for t in re.findall(r"[a-zàèéíóúüñ]+", s)
              if t not in ("i", "y", "and", "la", "el", "de", "es", "factura", "litres", "litros", "litre", "liters")]

    if not tokens:
        return None

    total = 0
    temp = 0
    for t in tokens:
        if t in units:
            temp += units[t]
        elif t in teens:
            temp += teens[t]
        elif t in tens:
            temp += tens[t]
        elif t in hundreds:
            # si hi havia una unitat prèvia (ex. "dos cents") multiplica; altrament assigna cent
            if temp == 0:
                temp = hundreds[t]
            else:
                temp = temp * hundreds[t]
        elif t.isdigit():
            temp += int(t)
        else:
            # token desconegut: s'ignora
            continue

    total += temp
    return total if total != 0 or ("zero" in tokens or "cero" in tokens) else None

def parse_litres(entrada):
    # Converteix una entrada de text a nombre de litres (gestiona coma decimal i text amb números)
    if entrada is None:
        raise ValueError("Entrada buida. Introdueix un número vàlid.")

    s = entrada.strip()
    if s == "":
        raise ValueError("Entrada buida. Introdueix un número vàlid.")

    # Accepta cadenes numèriques exactes (coma o punt com a separador)
    s_normal = s.replace(",", ".")
    if re.fullmatch(r'[-+]?\d+(\.\d+)?', s_normal):
        return float(s_normal)

    # Cerca la primera subcadena numèrica
    m = re.search(r'[-+]?\d+[.,]?\d*', s)
    if m:
        num_str = m.group().replace(",", ".")
        try:
            return float(num_str)
        except ValueError:
            pass

    # Prova de convertir paraules a nombre
    n = words_to_number(s)
    if n is not None:
        return float(n)

    # Si no es pot parsejar
    raise ValueError("Entrada no vàlida. Introdueix un número vàlid positiu o escriu 'sortir' per acabar.")

def mostrar_menu():
    # Mostra el menú, llegeix una entrada i gestiona la repetició sense utilitzar while True
    print("Càlcul de la factura de consum d'aigua")
    print("Introdueix els litres d'aigua consumits (escriu 'sortir' per acabar):")

    try:
        entrada = input("Litres consumits: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalitzat.")
        return

    if entrada.lower() in ['sortir', 'exit']:
        print("Programa finalitzat.")
        return

    try:
        litres = parse_litres(entrada)
        factura, operacio = calcular_factura(litres)
        print(f"Operació: {operacio}")
        print(f"Total a pagar: {factura:.2f} €\n")
    except ValueError as e:
        print(f"⚠ {e}\n")
    except Exception:
        # Captura errors inesperats per evitar que la terminal es bloquegi
        print("⚠ S'ha produït un error inesperat. Torna-ho a intentar.\n")

    try:
        repetir = input("Vols calcular una altra factura? (s/n): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalitzat.")
        return

    if repetir in ['s', 'si', 'y', 'yes']:
        mostrar_menu()
    else:
        print("Programa finalitzat.")

if __name__ == "__main__":
    mostrar_menu()
