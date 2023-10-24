def overenicisla(telcislo):
    if len(telcislo) == 9 or (telcislo[:4] == "+420" and len(telcislo) == 13):
        return True
    else:
        return False
def vypocetcenyzpravy(zprava):
    cena = (delka//180) * 3
    return cena
telcislo = input("Napiste telefonni cislo:")
if overenicisla(telcislo):
    zprava = input("Napiste text zpravy:")
    delka=len(zprava)+179
    cena = vypocetcenyzpravy(zprava)
    print(f"Cena zpravy je {cena} Kc.")
else:
    print("Telefonni cislo neni spravne.")


