'''
Creates users in Zendesk until its stopped.

@author: pchhetri
'''

print ("\n\nINFINITE USERS MAKER\n\n")
import requests
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
n = 0
u = 0
while 1:
	u +=1
	payload = '{"user": {"name": "Roger Wfiflco", "email": "roger%s@example.co.org", "verified": true, "role": "agent"}}' %(u)
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/users.json", data=payload)
	n+=1
	print payload
	print ("Created ticket #" + str(n) )
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")