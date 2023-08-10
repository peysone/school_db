"""
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników
(uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
Polecenie "koniec" - Kończy działanie aplikacji.

Proces tworzenia użytkowników:

Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia
 (jako jedna zmienna, można pobrać je jako dwie zmienne,
 jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela
(jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego,
a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy
(jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
Polecenie "koniec" - Wraca do pierwszego menu.

Proces zarządzania użytkownikami:

Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C")
program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia,
program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela,
program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela,
a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
Polecenie "koniec" - Wraca do pierwszego menu.

"""

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


uczniowie = []
nauczyciele = []
wychowawcy = []


def dodaj_ucznia():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    klasa = input("Podaj klasę ucznia: ")
    uczniowie.append(Uczen(imie, nazwisko, klasa))


def dodaj_nauczyciela():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    przedmiot = input("Podaj przedmiot prowadzony przez nauczyciela: ")
    klasy = []
    while True:
        klasa = input("Podaj klasę, którą prowadzi nauczyciel (wpisz pustą linię aby zakończyć): ")
        if not klasa:
            break
        klasy.append(klasa)
    nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))


def dodaj_wychowawce():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    klasa = input("Podaj klasę prowadzoną przez wychowawcę: ")
    wychowawcy.append(Wychowawca(imie, nazwisko, klasa))


def zarzadzaj_uczen():
    imie_ucznia = input("Podaj imię i nazwisko ucznia: ")
    for uczen in uczniowie:
        if imie_ucznia == f"{uczen.imie} {uczen.nazwisko}":
            print(f"Uczeń {uczen.imie} {uczen.nazwisko} należy do klasy {uczen.klasa}.")
            return
    print("Nie znaleziono takiego ucznia.")


def zarzadzaj_nauczyciel():
    nauczyciel = input("Podaj imię i nazwisko nauczyciela: ")
    for n in nauczyciele:
        if nauczyciel == f"{n.imie} {n.nazwisko}":
            print(f"Nauczyciel {n.imie} {n.nazwisko} prowadzi następujące klasy:")
            for klasa in n.klasy:
                print(klasa)
            return
    print("Nie znaleziono takiego nauczyciela.")


def zarzadzaj_wychowawca():
    wychowawca = input("Podaj imię i nazwisko wychowawcy: ")
    for w in wychowawcy:
        if wychowawca == f"{w.imie} {w.nazwisko}":
            print(f"Wychowawca {w.imie} {w.nazwisko} prowadzi klasę {w.klasa}.")
            uczniowie_wychowawcy = [uczen for uczen in uczniowie if uczen.klasa == w.klasa]
            print("Uczniowie w klasie:")
            for u in uczniowie_wychowawcy:
                print(f"{u.imie} {u.nazwisko}")
            return
    print("Nie znaleziono takiego wychowawcy.")


def zarzadzaj_klasa():
    klasa = input("Podaj nazwę klasy: ")
    print(f"Uczniowie w klasie {klasa}:")
    for u in uczniowie:
        if u.klasa == klasa:
            print(f"{u.imie} {u.nazwisko}")
    print("Nauczyciele prowadzący klasę:")
    for n in nauczyciele:
        if klasa in n.klasy:
            print(f"{n.imie} {n.nazwisko}")


def main():
    while True:
        print("1. Utwórz użytkownika")
        print("2. Zarządzaj użytkownikami")
        print("3. Koniec")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            print("1. Uczeń")
            print("2. Nauczyciel")
            print("3. Wychowawca")
            print("4. Koniec")
            numer = input("Wybierz rodzaj użytkownika do utworzenia: ")

            if numer == "1":
                dodaj_ucznia()
            elif numer == "2":
                dodaj_nauczyciela()
            elif numer == "3":
                dodaj_wychowawce()
            elif numer == "4":
                continue
            else:
                print("Nieprawidłowy wybór.")

        elif wybor == "2":
            print("1. Uczeń")
            print("2. Nauczyciel")
            print("3. Wychowawca")
            print("4. Klasa")
            print("5. Koniec")
            opcja = input("Wybierz opcję: ")

            if opcja == "1":
                zarzadzaj_uczen()
            elif opcja == "2":
                zarzadzaj_nauczyciel()
            elif opcja == "3":
                zarzadzaj_wychowawca()
            elif opcja == "4":
                zarzadzaj_klasa()
            elif opcja == "5":
                continue
            else:
                print("Nieprawidłowy wybór.")

        elif wybor == "3":
            break
        else:
            print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
