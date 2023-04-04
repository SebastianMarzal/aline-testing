import requests
import json

class AlineInterface:
  def __init__(self, port, username, password, host='localhost'):
    self.host = host
    self.port = str(port)
    self.username = username
    self.password = password
    self.auth = self.attempt_admin_login()
  
  def create_admin(self):
    admin = {
      "username": self.username,
      "password": self.password,
      "role": "admin",
      "firstName": "Admin",
      "lastName": "McAdminFace",
      "email": "adminface@smoothstack.com",
      "phone": "555 555 5555"
    }
    headers = {'Content-Type': 'application/json'}
    url = 'http://' + self.host + ':' + self.port + '/users' + '/registration'
    response = requests.post(url, json=admin, headers=headers)
    if response.status_code == 201:
      return self.attempt_admin_login()
    else:
      raise ValueError("Error code: {} returned.".format(response.status_code))
  
  def attempt_admin_login(self):
    credentials = {
      "username": self.username,
      "password": self.password
    }
    headers = {'Content-Type': 'application/json'}
    url = 'http://' + self.host + ':' + self.port + '/login'
    response = requests.post(url, json = credentials, headers = headers)
    auth = response.headers.get('Authorization', None)
    return auth if auth else self.create_admin()
  
  def authorized_headers(self):
    return {
      "Content-Type": "application/json",
      "Authorization": self.auth
    }