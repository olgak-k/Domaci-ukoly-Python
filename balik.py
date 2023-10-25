class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Status: {self.state}'


balik_1 = Package('Brno', 20, 'dorucen')
balik_2 = Package('Praha', 20, 'nedorucen')

seznam_baliku = [balik_1, balik_2]

print(balik_1.get_info())
print(balik_2.get_info())
print (f"Balik na adresu {self.address}, má hmotnost {self.weight} kg, je ve stavu {self.state}")

#Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
#Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
#Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.


