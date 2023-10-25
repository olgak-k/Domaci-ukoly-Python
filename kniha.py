#Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

#Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
#Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy, přičemž uvažuj, že přečtení jedné stránky zabere průměrnému čtenáři/čtenářce 4 minuty.
class Book:
    def __init__(self, title, pages, price):
        self.nazev = title
        self.strany = pages
        self.cena = price

    def get_info(self):
        return f'Nazev knihy je {self.nazev} a stoji {self.cena} korun'

    def get_time_to_read(self):
        minuty = 4 * self.strany
        return minuty // 60


kniha = Book('Zaklady Pythonu', 100, 10)
print(kniha.get_info())
print(kniha.get_time_to_read())