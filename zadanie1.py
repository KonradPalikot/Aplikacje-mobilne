class Film:
    def __init__(self):
        self._tytul = ""
        self._iloscWypozyczen = 0

    def ustaw_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł jest zbyt długi!")

    def pobierz_tytul(self):
        return self._tytul

    def zwieksz_ilosc_wypozyczen(self):
        self._iloscWypozyczen += 1

    def pobierz_ilosc_wypozyczen(self):
        return self._iloscWypozyczen


test = Film()

print(f"Tytul filmu: {test.pobierz_tytul()}")
print(f"Ilość wypożyczeń: {test.pobierz_ilosc_wypozyczen()}")

test.ustaw_tytul("test")
print(f"Tytul filmu: {test.pobierz_tytul()}")

test.zwieksz_ilosc_wypozyczen()
print(f"Ilość wypożyczeń: {test.pobierz_ilosc_wypozyczen()}")
