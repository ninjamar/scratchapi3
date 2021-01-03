#run 'pip install scratchapi3'
#in code
import scratchapi3
scratch = Scratch('username','password',csrf_token') #look in cookies to find it. Can someone help me get the cookie data from a website using python?
#comment
comment = Comment('csrf_token')
comment.profile_comment('content','parent_id','commentee_id','user') #can return
#cloud
cloud = Cloud()
cloud.cloudlog('project_id','limit','offset') #returns cloud log
#misc
misc = Misc()
misc = misc.message('user') #returns count
#login only - Beta
login_only = Login_Only('my_username') #- Nothing in class so useless
