#get the csrf token from chrome://settings/cookies/detail?site=scratch.mit.edu&search=cookies or clicking on the cookie icon on scratch
#to run use scratch = Login("USERNAME","PASSWORD","CSRF_TOKEN")
import requests
class Scratch:
  def get_csrf(self):
    #response = self.session.get('https://scratch.mit.edu/') 
    #return self.session.cookies.get_dict()
    pass
  def login(self):
    url = 'https://scratch.mit.edu/login/'
    login_data = {self.username: self.password,"csrfmiddlewaretoken":self.csrf_token}
    x = requests.post(url,headers={'referer': "https://scratch.mit.edu"},data=login_data)
    return x.text

  def __init__(self,username,password,csrf_token):
    self.username = username
    self.password = password
    self.csrf_token = csrf_token
    login()
    #self.session = requests.Session()

  def profile_comment(self,content,parent_id,commentee_id,user,csrf_token):
    url = f'https://scratch.mit.edu/site-api/comments/user/{user}/add/'
    data = {"content":content,"parent_id":parent_id,"commentee_id":commentee_id,"csrfmiddlewaretoken":csrf_token}
    x = requests.post(url=url,headers={'referer': "https://scratch.mit.edu"},data=data)
    return x.text

#CLOUD
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

#Random
  def messages(self,user):
    URL = f"https://api.scratch.mit.edu/users/{user}/messages/count"
    x = requests.get(url = URL)
    data = x.json()
    return data[1]
