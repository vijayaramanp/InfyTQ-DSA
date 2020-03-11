#DSA-Assgn-2
class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service:
    def __init__(self, car_list):
        self.__car_list=car_list
        
    def get_car_list(self):
        for car in self.__car_list:
            print(car)
            
    def find_cars_by_year(self,year):
        car_list_by_year=[]
        for car in self.__car_list:
            if car.get_year()==year:
                car_list_by_year.append(car.get_model())
        if len(car_list_by_year)>0:
            return car_list_by_year
        else:
             return None
    def add_cars(self,new_car_list):
        self.__car_list.extend(new_car_list)
        self.__car_list.sort(key=lambda x:x.get_year())
        
    def remove_cars_from_karnataka(self):
        self.__car_list=[x for x in self.__car_list if not x.get_registration_number().startswith("KA")]
        
car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car3, car5]
s1=Service(car_list)
s1.find_cars_by_year(2013)
new_car_list=[car1,car2,car4]
s1.add_cars(new_car_list)
s1.get_car_list()
s1.remove_cars_from_carnataka()
