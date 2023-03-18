import requests

class CompanyApi:
    
    def __init__(self, url):
        self.url = url
    
    def get_company_list(self, params_to_add = None):
        resp = requests.get(self.url+'/company/', params=params_to_add)
        return resp.json()
    
    def get_token(self, user = "michaelangelo", password = "party-dude"):
        creds = {
            "username": user,
            "password": password
        }

        resp = requests.post(self.url+'/auth/login/', json=creds)
        return resp.json()["userToken"]
    
    def get_company(self,  id):
        resp = requests.get(self.url+'/company/'+ str(id))
        return resp.json()
    
    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/company/', json=company, headers=my_headers)
        return resp.json()
   
    def edit(self, new_id, new_name, new_descr):
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        
        company = {
            "name": new_name,
            "description": new_descr
        }

        resp =requests.patch(self.url+'/company/'+ str(new_id), headers=my_headers, json=company)
        return resp.json()
    
    def delete(self, id):
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        
        resp =requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers)
        return resp.json()
    
    def set_active_state(self,id, isActive):
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()
        resp =requests.patch(self.url+'/company/status/'+ str(id), headers=my_headers, json= {'isActive': isActive})

        return resp.json()
    


#EMPLOYEE
    def get_company_employee(self,params_to_add):
        resp = requests.get(self.url+'/employee/', params=params_to_add)
        return resp.json()
    
    def post_new_employee(self, new_f_name, new_l_name, mew_m_name, new_phone):
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        employ = {
            "companyId": 1289,
            "firstName": new_f_name,
            "lastName": new_l_name,
            "middleName": mew_m_name,
            "phone": new_phone,
            "url": "string"
        }
        resp = requests.post(self.url+'/employee/', headers=my_headers, json=employ)
        return resp.json()
    
    def get_employee_id(self, id):
        resp = requests.get(self.url+'/employee/'+str(id))
        return resp.json()
    
    def edit_employee(self,id):
        my_headers ={}
        my_headers["x-client-token"] = self.get_token()

        new_employ = {
            "lastName": "Knazz",
            "email": "knazz@gmail.com",
            "url": "string",
            "isActive": True  # Я решил этот словарь не возводить в переменную. Мне кажется с точки зрения тестирования это не столь важно, так как тут меняются не все строки.
        }
        resp = requests.patch(self.url+'/employee/'+str(id),headers=my_headers, json=new_employ)
        return resp.json()