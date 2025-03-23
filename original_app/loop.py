import intro
import calcul

# ograniczenie liczby powtórzeń pętli
liczbaPowtórzeń = 4


def main():
    print("\nLICZBA KLASTRÓW ", calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    calcul.losujCentroidy()
    calcul.wypiszCentroidy()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    calcul.wypiszKlastry()

    # poniżej założono blokadę pętli
    repeat = 0
    while repeat < liczbaPowtórzeń:
        calcul.newCentroidy()
        calcul.wypiszCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        calcul.wypiszKlastry()
        repeat += 1


intro.wczytajDane()
