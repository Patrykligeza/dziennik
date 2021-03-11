from dziennik import Dziennik

dziennik = Dziennik(rok=2021, litera='b')
dziennik.dodaj_studenta('Janusz', nazwisko='Nowak', )
dziennik.dodaj_studenta('Piotr', nazwisko='Skowyrski')
student = dziennik.pobierz_studenta(1)
print(student.pobierz_srednia_ocen())
#print(dziennik.podaj_lilosc_studentow())