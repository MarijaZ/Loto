from random import randint

print("Dobrodosli v igri Loto!")
odgovor = int(raw_input("Koliko stevilk zelis izpisati: "))

def lotoo(kolicina_stevil):

    loto_stevila = []

    for naklj_stevilo in range(0,kolicina_stevil):

        naklj_stevilo = randint(0, 60)
        loto_stevila.append(naklj_stevilo)
    print(loto_stevila)
lotoo(odgovor)