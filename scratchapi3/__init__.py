import requests
import os
import linecache
class Scratch:
  def get_csrf(self):
    URL = 'https://scratch.mit.edu/login/'
    x = requests.get(url = URL)
    with open('login_token.txt','a') as f:
      f.write(x.text)
    line = linecache.getline('login_token.txt', 228)
    os.remove('login_token.txt')
    return line[55:87]
  def login(self):
    URL = 'https://scratch.mit.edu/login/'
    csrf_token = self.get_csrf()
    login_data = {self.username: self.password,"csrfmiddlewaretoken":csrf_token}
    x = requests.post(URL,headers={'referer': "https://scratch.mit.edu"},data=login_data)
    return x.text

  def __init__(self,username,password):
    self.username = username
    self.password = password
    self.login()



class Comment:
  def get_csrf():
    URL = 'https://scratch.mit.edu/login/'
    x = requests.get(url = URL)
    with open('login_token.txt','a') as f:
      f.write(x.text)
    line = linecache.getline('login_token.txt', 228)
    os.remove('login_token.txt')
    return line[55:87]

  def profile_comment(self,content,parent_id,commentee_id,user):
    URL = f'https://scratch.mit.edu/site-api/comments/user/{user}/add/'
    csrf_token = self.get_csrf()
    data = {"content":content,"parent_id":parent_id,"commentee_id":commentee_id,"csrfmiddlewaretoken":csrf_token}
    x = requests.post(url=url,headers={'referer': "https://scratch.mit.edu"},data=data)
    return x.text

class Cloud:
  def cloudLog(self,project_id,limit,offset):
    URL = f"https://clouddata.scratch.mit.edu/logs?projectid={project_id}&limit={limit}&offset={offset}"
    x = requests.get(url = URL)
    data = x.json()
    cloud = data[1]
    username = cloud["user"]
    action = cloud['verb']
    name = cloud['name']
    value = cloud['value']
    cloudList = [username,action,name,value]
    return cloudList

class Misc:
  def __init__(self,user):
    self.user = user
  def messages(self):
    URL = f"https://api.scratch.mit.edu/users/{self.user}/messages/count"
    x = requests.get(url = URL)
    data = x.json()
    return data[1]

class Login_Only:
  def get_csrf():
    URL = 'https://scratch.mit.edu/login/'
    x = requests.get(url = URL)
    with open('login_token.txt','a') as f:
      f.write(x.text)
    line = linecache.getline('login_token.txt', 228)
    os.remove('login_token.txt')
    return line[55:87]
  def __init__(self,my_username):
    self.path = 'https://scratch.mit.edu'
    self.csrf_token = self.get_csrf()
    self.username = my_username


  def follow(self,user):
    pass
  def unfollow(self,user):
    pass
