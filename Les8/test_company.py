import requests
from CompanyApi import CompanyApi
api = CompanyApi('https://x-clients-be.onrender.com')

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    full_list = api.get_company_list()
    filtred_list = api.get_company_list(params_to_add={'active':'true'})
    assert len(full_list) > len(filtred_list)

def test_add_new_companies():
    body = api.get_company_list()
    len_before = len(body)
    
    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name,descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)
    
    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id

def test_get_one_company():
    name = 'VS Code'
    descr = 'IDE'
    result = api.create_company(name,descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["isActive"] ==True

def test_edit_companies():
    name = 'Company to be edited'
    descr = 'Edit me'
    result = api.create_company(name,descr)
    new_id = result["id"]
    
    new_name ="UPDATED"
    new_descr = "__upd__"
    edited = api.edit(new_id, new_name, new_descr)
    assert edited["id"] == new_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] ==True

def test_delete_companies():
    name = 'Company to be deleted'
    result = api.create_company(name)
    new_id = result["id"]

    edited = api.delete(new_id)
    assert edited["id"] == new_id
    assert edited["name"] == name
    assert edited["description"] == ''
    assert edited["isActive"] ==True

    # body = api.get_company_list()
    # assert body[-1]["id"] != new_id

def test_deactivate_companies():
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    body = api.set_active_state(new_id, False)
    assert body["isActive"] == False

def test_deactivate_and_activate_back_companies():
    name = "Company to be activated"
    result = api.create_company(name)
    new_id = result["id"]
    
    api.set_active_state(new_id, False)
    body = api.set_active_state(new_id, True)
    assert body["isActive"] == True

def test_get_employee():
    body = api.get_company_employee(params_to_add={'company':'1289'})
    assert len(body) > 0

def test_new_employee():
    new_f_name = "Михаил"
    new_l_name = "Горшенев"
    mew_m_name = "Юрьевич"
    new_phone = "88005553535"
    
    new_employee = api.post_new_employee(new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    assert new_employee["id"] == new_id

def test_employee_id():
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_employee = api.post_new_employee(new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    
    
    body = api.get_employee_id(new_id)
    assert new_employee["id"] == new_id
    assert body["id"] == new_id
    
def test_edit_employee():
    new_f_name = "Андрей"
    new_l_name = "Князев"
    mew_m_name = "Сергеевич"
    new_phone = "88005553535"
    new_employee = api.post_new_employee(new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    body =api.edit_employee(new_id)
    
    assert new_employee["id"] == new_id
    assert body["email"] == "knazz@gmail.com"