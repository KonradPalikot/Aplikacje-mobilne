class Notatka:
    iloscNotatek = 0
    def __init__(self, tytul, tresc):
        Notatka.iloscNotatek += 1
        self._id = Notatka.iloscNotatek
        self._tytul = tytul
        self._tresc = tresc

    def zwrocNotatke(self):
        return(f"Tytuł: {self._tytul}\nTreść: {self._tresc}")

    def diagnostyka(self):
        return(f"ID: {self._id} ; Tytuł: {self._tytul} ; Treść: {self._tresc}")
    
notatka1 = Notatka("Notatka pierwsza", "Treść pierwszej notatki")
notatka2 = Notatka("Druga notatka", "Zawartość drugiej notatki")

print("Notatka1:")
print(notatka1.zwrocNotatke())
print(notatka1.diagnostyka())
print()
print("Notatka2:")
print(notatka2.zwrocNotatke())
print(notatka2.diagnostyka())