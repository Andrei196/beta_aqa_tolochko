import requests

class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
    
    def get_token(self, user = "michaelangelo", password = "party-dude"):
        creds = {
            "username": user,
            "password": password
        }

        resp = requests.post(self.url+'/auth/login/', json=creds)
        return resp.json()["userToken"]
    
    def get_company_employee(self,params_to_add):
        resp = requests.get(self.url+'/employee/', params=params_to_add)
        return resp.json()
    
    def post_new_employee(self, company_id, new_f_name, new_l_name, mew_m_name, new_phone):
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
            "isActive": True
        }
        resp = requests.patch(self.url+'/employee/'+str(id),headers=my_headers, json=new_employ)
        return resp.json()
    
    def edit_employee_none(self,id):
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
    
    def edit_employee_folse(self,id):
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