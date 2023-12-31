#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
#Vytvoř seznam průměrných teplot pro každý den.
#Vytvoř seznam ranních teplot.
#Vytvoř seznam nočních teplot.
#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
# Zadání seznamu teplot
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
prumerteplotden = [round(sum(den) / len(den),1) for den in teploty]
teplotarano = [den[0] for den in teploty]
teplotanoc = [den[-1] for den in teploty]
teplotypoledneanoc = [[den[1], den[-1]] for den in teploty]
print("prumer pro den: ", prumerteplotden)
print("teplota rano: ", teplotarano)
print("teplota v noci: ", teplotanoc)
print("seznam teplot: ", teplotypoledneanoc)