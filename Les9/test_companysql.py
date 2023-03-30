from CompanyApi import CompanyApi
from CompanySql import CompanySQL

api = CompanyApi('https://x-clients-be.onrender.com')
db = CompanySQL('postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients')

# def test_get_companies():
#     api_result = api.get_company_list()
#     db_result = db.get_companies()
#     assert len(api_result) == len(db_result)

# def test_get_active_companies():
#     filtred_list = api.get_company_list(params_to_add={'active':'true'})
#     db_list = db.get_active_companies()
#     assert len(filtred_list) == len(db_list)

# def test_add_new_companies():
#     body = api.get_company_list()
#     len_before = len(body)
    
#     name = "Autotest"
#     descr = "Descr"
#     result = api.create_company(name,descr)
#     new_id = result["id"]
   
#     body = api.get_company_list()
#     len_after = len(body)
#     db.delete(new_id)

#     assert len_after - len_before == 1
#     for company in body:
#         if company["id"] == new_id:
#             assert company["name"] == name
#             assert company["description"] == descr
#             assert company["id"] == new_id

# def test_get_one_company():
#     name = 'SkyPro'
#     db.create(name)
#     max_id = db.get_max_id()
#     new_company = api.get_company(max_id)
#     db.delete(max_id)
    
#     assert new_company["id"] == max_id
#     assert new_company["name"] == name
#     assert new_company["isActive"] ==True

# def test_edit_companies():
#     name = 'SkyPro'
#     db.create(name)
#     max_id = db.get_max_id()

#     new_name ="UPDATED"
#     new_descr = "__upd__"
#     edited = api.edit(max_id, new_name, new_descr)
#     db.delete(max_id)
#     assert edited["id"] == max_id
#     assert edited["name"] == new_name
#     assert edited["description"] == new_descr
#     assert edited["isActive"] ==True

# def test_delete_companies():
#     name = 'SkyPro'
#     db.create(name)
#     max_id = db.get_max_id()
#     deleted = api.delete(max_id)

    
#     assert deleted["id"] == max_id
#     assert deleted["name"] == name
#     assert deleted["isActive"] ==True
#     rows = db.get_company_by_id(max_id)
#     assert len(rows) == 1 

# def test_deactivate_companies():
#     name = 'SkyPro'
#     db.create(name)
#     max_id = db.get_max_id()
    
#     body = api.set_active_state(max_id, False)

#     assert body["isActive"] == False

# def test_deactivate_and_activate_back_companies():
#     name = 'SkyPro'
#     db.create(name)
#     max_id = db.get_max_id()

#     api.set_active_state(max_id, False)
#     body = api.set_active_state(max_id, True)
#     api.delete(max_id)
#     assert body["isActive"] == True


def test_get_employee():
    db_result = db.get_company_employee()
    assert len(db_result) > 0

def test_new_employee():
    name = 'КиШ'
    db.create(name)
    max_id = db.get_max_id()
    new_company = api.get_company(max_id)
    company_id = new_company
    
    new_f_name = "Михаил"
    new_l_name = "Горшенев"
    mew_m_name = "Юрьевич"
    new_phone = "88005553535"
    
    new_employee = api.post_new_employee(company_id, new_f_name, new_l_name, mew_m_name, new_phone)
    new_id = new_employee["id"]
    db.delete_employee(new_id)
    db.delete(max_id)
    
    assert new_employee["id"] == new_id

def test_employee_id():
    name = 'КиШ'
    db.create(name)
    max_id = db.get_max_id()
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

    body = api.get_employee_id(new_id)
    
    db.delete_employee(new_id)
    db.delete(max_id)

    assert body["id"] == new_id
    
def test_edit_employee():
    name = 'КиШ'
    db.create(name)
    max_id = db.get_max_id()
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

    body =api.edit_employee(new_id)
    db.delete_employee(new_id)
    db.delete(max_id)
    assert body["email"] == "knazz@gmail.com"