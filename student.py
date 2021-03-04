from typing import List
class Student:
    def __init__(self, imie , nazwisko, id):
        self.imie: str = imie
        self.nazwisko: str
        self.rok_urodzenia: int = 0
        self.pesel: int = 0
        self.id: int = 0
        self.oceny: List[int] = []