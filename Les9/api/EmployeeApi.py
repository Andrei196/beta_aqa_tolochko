import allure
import requests

class EmployeeApi:
    
    def __init__(self, url:str):
        self.url = url
    
    allure.step("(API) Получить токен авторизации {user}/{password}")
    def get_token(self, user:str = "michaelangelo", password:str = "party-dude")->str:
        """(API) Функция выполняет авторизацию"""
        creds = {
            "username": user,
            "password": password
        }

        resp = requests.post(self.url+'/auth/login/', json=creds)
        return resp.json()["userToken"]
    
    allure.step("(API) Проверить список сотрудников")
    def get_company_employee(self,params_to_add:None)->str:
        """(API) Функция выполняет GET запрос к сотрудникам"""
        resp = requests.get(self.url+'/employee/', params=params_to_add)
        return resp.json()
    
    allure.step("(API) Добавить нового сотрудника в компании с id{company_id}. Имя{new_f_name}, Фамилия{new_l_name}, Отчество{mew_m_name}, Телефон{new_phone}.")
    def post_new_employee(self, company_id:str, new_f_name:str, new_l_name:str, mew_m_name:str, new_phone:str)->dict:
        """(API) Функция выполняет создание нового сотрудника"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        employ = {
            "companyId": company_id,
            "firstName": new_f_name,
            "lastName": new_l_name,
            "middleName": mew_m_name,
            "phone": new_phone,
            "url": "string"
        }
        resp = requests.post(self.url+'/employee/', headers=my_headers, json=employ)
        return resp.json()
    
    allure.step("(API) Проверить наличие сотрудника по id {id}.")
    def get_employee_id(self, id:int)->None:
        """(API) Функция выполняет GET запрос к конкретному сотруднику"""
        resp = requests.get(self.url+'/employee/'+str(id))
        return resp.json()
    
    allure.step("(API) Отредактировать сотрудника с id {id}.")
    def edit_employee(self,id:int)->dict:
        """(API) Функция выполняет редактирование конкретного сотрудника"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        new_employ = {
            "lastName": "Knazz",
            "email": "knazz@gmail.com",
            "url": "string",
            "isActive": True
        }
        resp = requests.patch(self.url+'/employee/'+str(id),headers=my_headers, json=new_employ)
        return resp.json()
    
    allure.step("(API) Отредактировать сотрудника с id {id}. Оставить все редактируемые строки пустыми")
    def edit_employee_none(self,id:int)->dict: #Вот тут мне не понятно функция возвращает словарь или строку. Вроде бы просто строка, но и словарь тут не просто так.
        """(API) Функция выполняет редактирование конкретного сотрудника с(отсутствующеми значениями строк)"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        new_employ = {
            "lastName": "",
            "email": "",
            "url": "",
            "isActive": True
        }
        resp = requests.patch(self.url+'/employee/'+str(id),headers=my_headers, json=new_employ)
        return resp.json()
    
    allure.step("(API) Отредактировать сотрудника с id {id}. Заполнить все редактируемые строки невалидными данными")
    def edit_employee_folse(self,id:int)->dict:
        """(API) Функция выполняет редактирование конкретного сотрудника с(невалидными значениями строк)"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        new_employ = {
            "lastName": "$",
            "email": "#$$098^*&",
            "url": "♣",
            "isActive": True
        }
        resp = requests.patch(self.url+'/employee/'+str(id),headers=my_headers, json=new_employ)
        return resp.json()