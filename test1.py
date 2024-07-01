import string
def validare_pre_nume(cuv):
    x = 0
    for char in cuv:
        if char.isdigit():
            print("invalid:cifra introdusa")
            x = x + 1
            return False

        if char in string.punctuation:
            print("Invalid: caracter special introdus")
            x = x + 1
            return False





def validare_cnp(cnp):
    x = 0
    if len(cnp) != 13:
        print("Invalid: lungimea CNP-ului nu corespunde")
        return False


    if cnp.isdigit() != 1:
        print("Invalid: nu ati introdus cifre")
        return '!'
        x = x + 1


    if cifra_control(cnp) != int(cnp[12]):
        print("Invalid: CNP invalid")
        x = x + 1
    return x == 0

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

    for field in date:
        if not field.strip():
            print("Invalid: date incomplete")
            return False
        break
    return True


lista_cursanti = []
i = 1
while i:

    print("Introduceti date cursant")
    prenume = input("Prenume")
    while (validare_pre_nume(prenume) == False ) :
        prenume = input("Prenume")


    nume = input("Nume")
    while (validare_pre_nume(nume) == False):
        nume = input("Nume")

    CNP = input("CNP")
    while (validare_cnp(CNP) == False ):
        CNP = input("CNP")


    date_cursant =[prenume, nume, CNP]
    while (validare_date(date_cursant) == False ):
        CNP = input("CNP")

    print("Datele cursantului", prenume, nume, CNP)

    cursant = {
        "prenume": prenume,
        "nume": nume,
        "CNP": CNP
            }

    lista_cursanti.append(cursant)

    i = int(input("Adaugati cursant? \n 1-da, 0-nu \n"))
    if i == 0:
        break

print("Lista finală a cursanților:")
for i, cursant in enumerate(lista_cursanti, start=1):
    print(f"Cursantul {i}: {cursant['prenume']} {cursant['nume']} - CNP: {cursant['CNP']}")


print("Lista cursantilor ordonati alfabetic")
lista_cursanti.sort(key=lambda cursant: cursant['nume'])
for i, cursant in enumerate(lista_cursanti, start=1):
    sorted_cursant = dict(sorted(cursant.items()))
    print(f"Cursant: {sorted_cursant}")


salvare = int(input("Doriti sa salvati? \n 1-da, 0-nu \n "))
if salvare:
    file = "cursanti.txt"

    with open(file, 'w') as f:
        for cursant in lista_cursanti:
            f.write(f"Prenume: {cursant['prenume']}, Nume: {cursant['nume']}, CNP: {cursant['CNP']}\n")

    print("Fisier salvat")

