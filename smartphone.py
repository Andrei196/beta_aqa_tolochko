class Smartphone:
    def __init__ (self, make, model, number):
        self.i_make = make
        self.i_model = model
        self.i_number = number
   
    def phone(self):
        print("Марка телефона ",self.i_make)
        print("Модель телефона ",self.i_model)
        print("Абонентский номер",self.i_number)