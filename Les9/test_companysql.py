import allure
from api.CompanyApi import CompanyApi
from api.EmployeeApi import EmployeeApi
from db.CompanySql import CompanySQL
from db.EmployeeSql import EmployeeSQL

company_api = CompanyApi('https://x-clients-be.onrender.com')
employee_api = EmployeeApi('https://x-clients-be.onrender.com')
company_db = CompanySQL('postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients')
employee_db = EmployeeSQL('postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients')

@allure.epic("Сотрудник")
@allure.id("SQL-1")
@allure.story("Проверка списка сотрудников")
@allure.feature("READ")
@allure.title("Проверить отображение сотрудников в базе данных")
@allure.severity("CRITICAL")
def test_get_employee():
    db_result = employee_db.get_company_employee()
    with allure.step("Сравнение ФР с ОР"):
        assert len(db_result) > 0

@allure.epic("Сотрудник")
@allure.id("SQL-2")
@allure.story("Добавить сотрудника")
@allure.feature("CREATE")
@allure.title("Проверить создание нового сотрудника в базе данных")
@allure.description("Число сотрудников должно увеличится на один")
@allure.severity("CRITICAL")
def test_new_employee():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    new_company = company_api.get_company(max_id)
    company_id = new_company
    
    new_f_name = "Михаил"
    new_l_name = "Горшенев"
    mew_m_name = "Юрьевич"
    new_phone = "88005553535"
    
    new_employee = employee_api.post_new_employee(company_id, new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Получить информацию о добавление новой компании"):
        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["isActive"] ==True
    
    with allure.step("Получить информацию о добавление нового сотрудника"):
        assert new_employee["id"] == new_id
        assert len(new_employee) == 1

@allure.epic("Сотрудник")
@allure.id("SQL-3")
@allure.story("Добавить сотрудника")
@allure.feature("CREATE")
@allure.title("Проверить создание нового сотрудника в базе данных с пустыми значениями")
@allure.description("Число сотрудников должно увеличится на один")
@allure.severity("BLOCKADE")
def test_new_employee_None():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    new_company = company_api.get_company(max_id)
    company_id = new_company
    
    new_f_name = ""
    new_l_name = ""
    mew_m_name = ""
    new_phone = ""
    
    new_employee = employee_api.post_new_employee(company_id, new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Получить информацию о добавление новой компании"):
        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["isActive"] ==True
    
    with allure.step("Получить информацию о добавление нового сотрудника"):
        assert new_employee["id"] == new_id
        assert len(new_employee) == 1

@allure.epic("Сотрудник")
@allure.id("SQL-4")
@allure.story("Добавить сотрудника")
@allure.feature("CREATE")
@allure.title("Проверить создание нового сотрудника в базе данных с невалидными значениями")
@allure.description("Число сотрудников должно увеличится на один")
@allure.severity("BLOCKADE")
def test_new_employee_Folse():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    new_company = company_api.get_company(max_id)
    company_id = new_company
    
    new_f_name = "☺"
    new_l_name = "☻"
    mew_m_name = "♥"
    new_phone = "♦♣♠♥•◘○☺☻♥♫↓$:/"
    
    new_employee = employee_api.post_new_employee(company_id, new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Получить информацию о добавление новой компании"):
        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["isActive"] ==True
    
    with allure.step("Получить информацию о добавление нового сотрудника"):
        assert new_employee["id"] == new_id
        assert len(new_employee) == 1

@allure.epic("Сотрудник")
@allure.id("SQL-5")
@allure.story("Проверка конкретного сотрудника")
@allure.feature("READ")
@allure.title("Проверить отображение сотрудника в базе данных")
@allure.severity("CRITICAL")
def test_employee_id():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    company = company_api.get_company(max_id)
    
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_email = "Knazz@gmail.com"
    new_url = "string"
    new_company =company["id"]
    employee_db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = employee_db.employee_max_id()

    get_employee = employee_api.get_employee_id(new_id)
    
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Сравнение ФР с ОР"):
        assert get_employee["id"] == new_id
        assert get_employee["firstName"] == new_f_name
        assert get_employee["lastName"] == new_l_name
        assert get_employee["middleName"] == mew_m_name
        assert get_employee["phone"] == new_phone
        assert get_employee["email"] == new_email
        assert get_employee["avatar_url"] == new_url
        assert get_employee["companyId"] == new_company

@allure.epic("Сотрудник")
@allure.id("SQL-6")
@allure.story("Редактирование сотрудника")
@allure.feature("EDITED")
@allure.title("Проверка редактирования сотрудника в базе данных")
@allure.description("Для редактирования сотрудника используется ID существующего сотрудника")
@allure.severity("CRITICAL")    
def test_edit_employee():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    company = company_api.get_company(max_id)
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_email = "Kish@gmail.com"
    new_url = "string"
    new_company =company["id"]
    employee_db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = employee_db.employee_max_id()

    edit_employee =employee_api.edit_employee(new_id)
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Сравнение ФР с ОР"):
        assert edit_employee["id"] == new_id
        assert edit_employee["email"] == "knazz@gmail.com"
        assert edit_employee["isActive"] == True
        assert edit_employee["url"] == new_url

@allure.epic("Сотрудник")
@allure.id("SQL-7")
@allure.story("Редактирование сотрудника")
@allure.feature("EDITED")
@allure.title("Проверка редактирования сотрудника в базе данных с добавлением пустых значений в редактируемые строках")
@allure.description("Для редактирования сотрудника используется ID существующего сотрудника")
@allure.severity("CRITICAL")  
def test_edit_employee_none():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    company = company_api.get_company(max_id)
    new_f_name = ""
    new_l_name = ""
    mew_m_name = ""
    new_phone = ""
    new_email = ""
    new_url = ""
    new_company =company["id"]
    employee_db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = employee_db.employee_max_id()

    edit_employee =employee_api.edit_employee_none(new_id)
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Сравнение ФР с ОР"):
        assert edit_employee["id"] == new_id
        assert edit_employee["email"] == ""
        assert edit_employee["isActive"] == True
        assert edit_employee["url"] == ""

@allure.epic("Сотрудник")
@allure.id("SQL-8")
@allure.story("Редактирование сотрудника")
@allure.feature("EDITED")
@allure.title("Проверка редактирования сотрудника в базе данных с добавлением невалидных значений в редактируемые строках")
@allure.description("Для редактирования сотрудника используется ID существующего сотрудника")
@allure.severity("CRITICAL")  
def test_edit_employee_folse():
    name = 'КиШ'
    company_db.create_company(name)
    max_id = company_db.get_max_id_company()
    company = company_api.get_company(max_id)
    new_f_name = "☺"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_email = "Kish@gmail.com"
    new_url = "string"
    new_company =company["id"]
    employee_db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = employee_db.employee_max_id()

    edit_employee =employee_api.edit_employee_folse(new_id)
    employee_db.delete_employee(new_id)
    company_db.delete_company(max_id)
    
    with allure.step("Сравнение ФР с ОР"):
        assert edit_employee["id"] == new_id
        assert edit_employee["email"] == "#$$098^*&"
        assert edit_employee["isActive"] == True
        assert edit_employee["url"] == "♣"