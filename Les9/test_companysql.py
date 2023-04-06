from CompanyApi import CompanyApi
from CompanySql import CompanySQL

api = CompanyApi('https://x-clients-be.onrender.com')
db = CompanySQL('postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients')

def test_get_employee():
    db_result = db.get_company_employee()
    assert len(db_result) > 0

def test_new_employee():
    name = 'КиШ'
    db.create_company(name)
    max_id = db.get_max_id_company()
    new_company = api.get_company(max_id)
    company_id = new_company
    
    new_f_name = "Михаил"
    new_l_name = "Горшенев"
    mew_m_name = "Юрьевич"
    new_phone = "88005553535"
    
    new_employee = api.post_new_employee(company_id, new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    db.delete_employee(new_id)
    db.delete_company(max_id)
    
    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["isActive"] ==True
    
    assert new_employee["id"] == new_id
    assert len(new_employee) == 1

def test_employee_id():
    name = 'КиШ'
    db.create_company(name)
    max_id = db.get_max_id_company()
    company = api.get_company(max_id)
    
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_email = "Knazz@gmail.com"
    new_url = "string"
    new_company =company["id"]
    db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = db.employee_max_id()

    get_employee = api.get_employee_id(new_id)
    
    db.delete_employee(new_id)
    db.delete_company(max_id)
    
    assert get_employee["id"] == new_id
    assert get_employee["firstName"] == new_f_name
    assert get_employee["lastName"] == new_l_name
    assert get_employee["middleName"] == mew_m_name
    assert get_employee["phone"] == new_phone
    assert get_employee["email"] == new_email
    assert get_employee["avatar_url"] == new_url
    assert get_employee["companyId"] == new_company
    
def test_edit_employee():
    name = 'КиШ'
    db.create_company(name)
    max_id = db.get_max_id_company()
    company = api.get_company(max_id)
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_email = "Kish@gmail.com"
    new_url = "string"
    new_company =company["id"]
    db.new_employee(new_f_name, new_l_name, mew_m_name, new_phone, new_email, new_url, new_company)
    new_id = db.employee_max_id()

    edit_employee =api.edit_employee(new_id)
    db.delete_employee(new_id)
    db.delete_company(max_id)
    
    assert edit_employee["id"] == new_id
    assert edit_employee["email"] == "knazz@gmail.com"
    assert edit_employee["isActive"] == True
    assert edit_employee["url"] == new_url