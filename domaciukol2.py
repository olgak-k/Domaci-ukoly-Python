sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kodsoucastky = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte požadované množství: "))

if kodsoucastky in sklad:
    mnozstviskladem = sklad[kodsoucastky]
    if mnozstvi <= mnozstviskladem:
        print(f"{kodsoucastky} je skladem a je k dispozici {mnozstviskladem} ks, poptávku lze uspokojit v plné výši.")
        sklad[kodsoucastky] = sklad[kodsoucastky] - mnozstvi
    else:
        print(f"Skladem je pouze {mnozstviskladem} ks {kodsoucastky}.")
        del sklad[kodsoucastky]
else:
    print(f"{kodsoucastky} není skladem.")