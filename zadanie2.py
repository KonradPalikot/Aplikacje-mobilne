class Osoba:
    liczbaInstancji = 0
    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        self.test = "qwerty"
        Osoba.liczbaInstancji += 1

    def Kopiowanie(self, osoba):
        return Osoba(osoba.__id, osoba.__imie)

osoba1 = Osoba(1, "Imie")
osoba2 = osoba1.Kopiowanie(osoba1)
osoba2.test = "test"
print(osoba1)
print(osoba2)
print(Osoba.liczbaInstancji)
