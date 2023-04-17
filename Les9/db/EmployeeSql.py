import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeSQL:
    __scripts = {
        "select employee" : text("SELECT * FROM employee"),
        "new employee" : text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"phone\", \"email\", \"avatar_url\", \"companyId\") values (:f_name,:l_name, :m_name, :phone, :email, :url, :company_id)"),
        "employee max id" : text("select MAX(id) from employee"),
        "delete employee" :text("delete from employee where id = :id_to_delete"),
        }

    def __init__(self, connection_string)->None:
        self.__db = create_engine(connection_string)
    
    allure.step("(db) Проверить список сотрудников.")
    def get_company_employee(self)->str:
        """(db) Функция выполняет запрос к списку сотрудников"""
        query = self.__db.execute(self.__scripts["select employee"])
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()
    
    allure.step("(db) Добавить нового пользователя с данными: Имя:{new_f_name}, Фамилия:{new_l_name}, Отчество:{mew_m_name}, Телефон:{new_phone}, Почта:{new_email}, URL:{new_url}, Компания:{new_company}.")
    def new_employee(self, new_f_name:str, new_l_name:str, mew_m_name:str, new_phone:str, new_email:str, new_url:str, new_company:str)->str:
        """(db) Функция выполняет добавление нового сотрудника"""
        query = self.__db.execute(self.__scripts["new employee"], f_name=new_f_name, l_name=new_l_name, m_name=mew_m_name, phone=new_phone, email=new_email, url=new_url, company_id=new_company)
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
    
    allure.step("(db) Получить максимальный id среди сотрудников.")
    def employee_max_id(self)->str:
        """(db) Функция выполняет запрос к максимальному значению по id в списке сотрудников"""
        query = self.__db.execute(self.__scripts["employee max id"])
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()[0][0]
    
    allure.step("(db) Удалить сотрудника с id{id}.")
    def delete_employee(self,id:int)->str:
        """(db) Функция выполняет удаление конкретного сотрудника"""
        query = self.__db.execute(self.__scripts["delete employee"], id_to_delete = id)
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        # Я вам честно скажу, что не понял до конца принцип постановки возвращаемых данных. Я рассуждаю с точки зрения, что так выглядит лучше.