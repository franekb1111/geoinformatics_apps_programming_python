class Ponowna_rezerwacja_tego_samego_miejsca(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


miejsca = [{"nr_miejsca": 'A2', "rzad":2, "rezerwacja": False}, {"nr_miejsca": 'B3', "rzad":3, "rezerwacja": False}, {"nr_miejsca": 'C1', "rzad":1, "rezerwacja": False}]

def zarezerwuj_miejsce(nr_miejsca,imie_nazwisko):
    try:
        for miejsce in miejsca:
            if miejsce.get("uzytkownik") == imie_nazwisko:
                raise Ponowna_rezerwacja_tego_samego_miejsca(f"Użytkownik już zarezerwował to miejsce.")
    except Ponowna_rezerwacja_tego_samego_miejsca as e:
        return print(str(e))
    try:
        if(sum(miejsce["rezerwacja"] for miejsce in miejsca) == 3):
            raise ValueError("Brak miejsc na seans")
    except ValueError as e:
        return print(str(e))
    try:
        for miejsce in miejsca:
            if nr_miejsca == miejsce['nr_miejsca']:
                if miejsce['rezerwacja']:
                    raise ValueError("To miejsce już jest zarezerwowane")
                else:
                    miejsce["rezerwacja"] = True
                    miejsce["uzytkownik"] = imie_nazwisko
                    print(f"Miejsce {nr_miejsca} zostało zarezerwowane przez {imie_nazwisko}.")
    except ValueError as e:
        return print(str(e))

def anuluj_rezerwacje(nr_miejsca, imie_nazwisko):
    try:
        for miejsce in miejsca:
            if (miejsce.get("uzytkownik") == imie_nazwisko) & (miejsce['nr_miejsca'] == nr_miejsca) & (miejsce['rezerwacja'] == True):
                miejsce['rezerwacja'] = False
                miejsce['uzytkownik'] = None
                return print("Anulowano rezerwację")
        raise ValueError("Złe imię i nazwisko, nr miejsca lub miejsce nie zostało wcześniej zarezerwowane ")
    except ValueError as e:
        return print(str(e))

zarezerwuj_miejsce('A2', "Jan Kowalski")
print()
zarezerwuj_miejsce('A2', "Jan Kowalski")
print()
zarezerwuj_miejsce('B3', "Krzysztof Nowak")
print()
zarezerwuj_miejsce('B3', "Anna Kowalska")
print()
zarezerwuj_miejsce('C1', "Krzysztof Wrona")
print()
zarezerwuj_miejsce('C1', "Marta Polna")
print()

anuluj_rezerwacje('C1', "Marta Polak")
print()
anuluj_rezerwacje('C1', "Krzysztof Wrona")

print()
print(miejsca)
print()

zarezerwuj_miejsce('C1', "Krystyna Szwed")


    

    
    


