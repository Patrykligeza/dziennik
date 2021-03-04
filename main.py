from dziennik import Dziennik

d = Dziennik(rok=2021, litera='b')
d.dodaj_studenta('Janusz', 'Nowak',)
d.dodaj_studenta('Piotr', 'Skowyrski')

print(d.podaj_lilosc_studentow())