class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def sayName(self):
        print("Имя ", self.f_name)
        print("Фамилия ", self.l_name)
        print("Имя и Фамилия",self.f_name, self.l_name)
        