import allure
import requests

class CompanyApi:
    
    def __init__(self, url:str):
        self.url = url
    
    allure.step("(API) Проверить список компаний")
    def get_company_list(self, params_to_add = None)->str:
        """(API) Функция выполняет GET запрос к списку компаний"""
        resp = requests.get(self.url+'/company/', params=params_to_add)
        return resp.json()
    
    allure.step("(API) Получить токен авторизации {user}/{password}")
    def get_token(self, user:str = "michaelangelo", password:str = "party-dude")->str:
        """(API) Функция выполняет авторизацию"""
        creds = {
            "username": user,
            "password": password
        }

        resp = requests.post(self.url+'/auth/login/', json=creds)
        return resp.json()["userToken"]
    
    allure.step("(API) Проверить наличие компании по id {id}")
    def get_company(self,  id:int)->str:
        """(API) Функция выполняет GET запрос к конкретной компании"""
        resp = requests.get(self.url+'/company/'+ str(id))
        return resp.json()
    
    allure.step("(API) Добавить новую компанию с названием например,:{name}. Описанием, например:{description}.")
    def create_company(self, name:str, description:str='')->None:
        """(API) Функция выполняет добавление новой компании"""
        company = {
            "name": name,
            "description": description
        }
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/company/', json=company, headers=my_headers)
        return resp.json()
   
    allure.step("(API) Отредактировать компанию с id :{new_id}. Заменить название на:{new_name}. Заменить описание, на:{new_descr}.")
    def edit_company(self, new_id:int, new_name:str, new_descr:str)->None:
        """(API) Функция выполняет редактирование конкретной компании"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        
        company = {
            "name": new_name,
            "description": new_descr
        }

        resp =requests.patch(self.url+'/company/'+ str(new_id), headers=my_headers, json=company)
        return resp.json()
    
    allure.step("(API) Удалить компанию с id :{id}.")
    def delete_company(self, id:int)->None:
        """(API) Функция выполняет удаление конкретной компании"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        
        resp =requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers)
        return resp.json()
    
    allure.step("(API) Проверить активность компании с id :{id}. isActive={isActive}.")
    def set_active_state_company(self,id:int, isActive:bool)->bool:
        """(API) Функция выполняет проверку активоности компании"""
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        resp =requests.patch(self.url+'/company/status/'+ str(id), headers=my_headers, json= {'isActive': isActive})

        return resp.json()