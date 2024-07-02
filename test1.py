
import string


def validare_pre_nume(cuv):
    x = 0
    try:
        for char in cuv:
            if char.isdigit():
                raise ValueError("Invalid: cifra introdusa")
            if char in string.punctuation:
                raise ValueError("Invalid: caracter special introdus")
        return True
    except ValueError as e:
        print(e)
        x += 1
        return False


def validare_cnp(cnp):
    x = 0
    try:
        if len(cnp) != 13:
            raise ValueError("Invalid: lungimea CNP-ului nu corespunde")
        if not cnp.isdigit():
            raise ValueError("Invalid: nu ati introdus cifre")
        if cifra_control(cnp) != int(cnp[12]):
            raise ValueError("Invalid: CNP invalid")
        return True
    except ValueError as e:
        print(e)
        x += 1
        return False


def cifra_control(cnp):
    constanta = '279146358279'
    suma = 0
    for i in range(12):
        suma = suma + int(cnp[i]) * int(constanta[i])
    ctrl = suma % 11
    if ctrl == 10:
        ctrl = 1
    return ctrl


def validare_date(date):
    try:
        for field in date:
            if not field.strip():
                raise ValueError("Invalid: date incomplete")
        return True
    except ValueError as e:
        print(e)
        return False


lista_cursanti = []
i = 1
while i:
    print("Introduceti date cursant")

    prenume = input("Prenume: ")
    while not validare_pre_nume(prenume):
        prenume = input("Prenume: ")

    nume = input("Nume: ")
    while not validare_pre_nume(nume):
        nume = input("Nume: ")

    CNP = input("CNP: ")
    while not validare_cnp(CNP):
        CNP = input("CNP: ")

    date_cursant = [prenume, nume, CNP]
    while not validare_date(date_cursant):
        CNP = input("CNP: ")

    print(f"Datele cursantului: {prenume} {nume} {CNP}")

    cursant = {
        "prenume": prenume,
        "nume": nume,
        "CNP": CNP
    }

    lista_cursanti.append(cursant)

    try:
        i = int(input("Adaugati cursant? \n 1-da, 0-nu \n"))
    except ValueError:
        print("Trebuie să introduceți 1 sau 0.")
        continue

    if i == 0:
        break

print("Lista finală a cursanților:")
for i, cursant in enumerate(lista_cursanti, start=1):
    print(f"Cursantul {i}: {cursant['prenume']} {cursant['nume']} - CNP: {cursant['CNP']}")

print("Lista cursanților ordonati alfabetic")
lista_cursanti.sort(key=lambda cursant: cursant['nume'])
for i, cursant in enumerate(lista_cursanti, start=1):
    sorted_cursant = dict(sorted(cursant.items()))
    print(f"Cursant: {sorted_cursant}")

try:
    salvare = int(input("Doriți să salvați? \n 1-da, 0-nu \n "))
    if salvare:
        file = "cursanti.txt"
        with open(file, 'w') as f:
            for cursant in lista_cursanti:
                f.write(f"Prenume: {cursant['prenume']}, Nume: {cursant['nume']}, CNP: {cursant['CNP']}\n")
        print("Fișier salvat")
except ValueError:
    print("Trebuie să introduceți 1 sau 0.")
