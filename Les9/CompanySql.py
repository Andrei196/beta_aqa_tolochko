from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanySQL:
    __scripts = {
        "select" : "select * from company",
        "select by id" : text("select * from company where id = :select_id"),
        "select only active" : text("select * from company where \"isActive\" = true"),
        "delete by id" :text("delete from company where id = :id_to_delete"),
        "insert new" : text("insert into company(\"name\") values (:new_name)"),
        "get max id" : text("select MAX(id) from company"),
        "select employee" : text("SELECT * FROM employee"),
        "new employee" : text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"phone\", \"email\", \"avatar_url\", \"companyId\") values (:f_name,:l_name, :m_name, :phone, :email, :url, :company_id)"),
        "employee max id" : text("select MAX(id) from employee"),
        "delete employee" :text("delete from employee where id = :id_to_delete"),
        
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
    
    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()
    
    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id =id ).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select only active"]).fetchall()
    
    def delete_company(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create_company(self, name):
        self.__db.execute(self.__scripts["insert new"], new_name = name)
    
    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]
    
    def get_company_employee(self):
        return self.__db.execute(self.__scripts["select employee"]).fetchall()
    
    def new_employee(self, new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company):
        self.__db.execute(self.__scripts["new employee"], f_name=new_f_name, l_name=new_l_name, m_name=mew_m_name, phone=new_phone, email=new_email, url=new_url, company_id=new_company)

    def employee_max_id(self):
        return self.__db.execute(self.__scripts["employee max id"]).fetchall()[0][0]
    
    def delete_employee(self,id):
        self.__db.execute(self.__scripts["delete employee"], id_to_delete = id)