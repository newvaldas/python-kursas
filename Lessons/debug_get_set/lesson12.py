from random import randint
from typing import Optional


class Workers:
    def __init__(self, name, surname, wage):
        self.name = name
        self.surname = surname
        self.__wage = wage

    def calc_avergae(self):
        return self.__wage // 10

    
    @property                       # su property galime pasigaminti nauja klases atributa(legva iskviesti nes ner aprivate ar protected)
    def wage_after(self) -> int:
        return  self.__wage

    @wage_after.setter                          # setina funkcija kaip set_wage kur auksciau apsiraseme
    def wage_after(self,) -> int:
        return self.__wage

class Company:
    def __init__(self):
        self.worker = Workers("Antanas", "Antanauskas", 650)
    
    def get_company_financials(self):
        return self.worker.wage_after

    def get_random_number(self, number: int) -> Optional[int]:
        try:
            nr = randint(0, 100)
            if type(number) != int:
                raise ValueError("Not the value I wanted")
            return number - nr + self.get_company_financials()
        except Exception:
            pass

my_company = Company()
print(my_company.get_random_number(25.25))


