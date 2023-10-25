import json
with open('body.json', mode='r', encoding='utf-8') as file:
    pisemka=json.load(file) 
vysledek= {}
for jmeno, body in pisemka.items():
    if body >= 60:
     vysledek[jmeno]="Pass"
    else:
     vysledek[jmeno]="Fail"
with open('prospech.json', mode='w', encoding='utf-8') as file:
 json.dump(vysledek,file, ensure_ascii=False)

