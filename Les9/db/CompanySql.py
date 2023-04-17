import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanySQL:
    __scripts:dict = {
        "select" : text("select * from company"),
        "select by id" : text("select * from company where id = :select_id"),
        "select only active" : text("select * from company where \"isActive\" = true"),
        "delete by id" :text("delete from company where id = :id_to_delete"),
        "insert new" : text("insert into company(\"name\") values (:new_name)"),
        "get max id" : text("select MAX(id) from company"),
    }

    def __init__(self, connection_string)->None:
        self.__db = create_engine(connection_string)
    
    allure.step("(db) Проверить список компаний.")
    def get_companies(self)->str:
        """(db) Функция выполняет запрос к списку компаний"""
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()
    
    allure.step("(db) Проверить наличие компании по id {id}.")
    def get_company_by_id(self, id:int)->str:
        """(db) Функция выполняет запрос к конкретной компании"""
        query = self.__db.execute(self.__scripts["select by id"], select_id =id)
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()
    
    allure.step("(db) Проверить активность компаний.")
    def get_active_companies(self)->str:
        """(db) Функция выполняет запрос к списку активных компаний"""
        query = self.__db.execute(self.__scripts["select only active"])
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()
    
    allure.step("(db) Удалить компанию с id :{id}.")
    def delete_company(self, id:int)->str:
        """(db) Функция выполняет удаление компании"""
        query = self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
    
    allure.step("(db) Добавить новую компанию с названием например,:{name}.")
    def create_company(self, name:str)->str:
        """(db) Функция выполняет добавление новой компании"""
        query = self.__db.execute(self.__scripts["insert new"], new_name = name)
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
    
    allure.step("(db) Получить максимальный id среди компаний.")
    def get_max_id_company(self)->str:
        """(db) Функция выполняет запрос к максимальному значению по id в списке компаний"""
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.query), "SQL",allure.attachment_type.TEXT)
        return query.fetchall()[0][0]