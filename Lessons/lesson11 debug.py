# class Workers:
#     def __init__(self, name, surname, wage):
#         self.name = name
#         self.surname = surname
#         self.__wage = wage

#     def calc_avergae(self):
#         return self.__wage // 10

    
#     @property                       # su property galime pasigaminti nauja klases atributa(legva iskviesti nes ner aprivate ar protected)
#     def wage_after(self) -> int:
#         return  5 * self.__wage

#     def set_wage(self, new_wage: int) -> int:
#         self.__wage - new_wage
    
#     # @wage_after.setter                          # setina funkcija kaip set_wage kur auksciau apsiraseme
#     # def wage_after(self,) -> int:
#     #     return self.__wage



    
      
 


# antanas = Workers("Antanas", "Antanauskas", 650)

# antanas.wage_after = 150        #abu atitinka tokia pat israiska
# antanas.set_wage(150)           #abu atitinka tokia pat israiska


# class Company:
#     def __init__(self):
#         self.worker = Workers("Antanas", "Antanauskas", 650)
    
#     def get_company_financials(self):
#         return self.worker.wage_after

# uzduotis
#Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte". 
# Padaryti taip, kad savybė "verte" koreguojama tik įvedus skaičių. Programoje naudoti dekoratorių @property.


class House:
    def __init__(self, area: str, value: int):
        self.area = area
        self.__value =  value

    @property
    def set_value (self) -> int:
        return self.__value

    @set_value.setter 
    def set_value(self, new: int) -> None:
        if new < 0:
            print("Value cant be negative")
        else:
            self.__value = new
    
house1 = House ("New location", 232422)

print(house1.set_value)

house1.set_value = 350000
print(house1.set_value)

# 2 uzduotis

class Car:

    def __init__(self, year:int, model:str, fuel_type: str):

        self.year = year
        self. model = model
        self.fuel_type = fuel_type

    def drivinig(self):
        print("Driving")

    def standing_still(self):
        print("Not moving")

    def refueling(self):
        print("Refueling")

    def give_info(self):
        return f'Made year is: {self.year}, model is is: {self.model}, fueal type is: {self.fuel_type}'

    

class Electric(Car):

    def refueling(self):
        print("Battery charged")

    def drive_autonomus(self):
        print("Driving auto")

audi = Car(2010, "A8", "Petrol")
tesla = Electric(2015, "Model S", "Electricity")

print(audi.give_info())


audi.drivinig()
audi.standing_still()
audi.refueling()   

tesla.drivinig()
tesla.standing_still()
tesla.refueling()   