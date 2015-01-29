'''
Deletes objects from a Zendesk endpoint. The following deletes all users from Zendesk 

@author: pchhetri
'''

print ("\n\nTHE DESTROYER\n\n")
import requests
import json
s = requests.Session()
s.auth = ('USR','PASS')
while 1:
	r = s.get("https://SUBDOMAIN.zendesk.com/api/v2/users.json")
	data = json.loads(r.text)
	for each in data['users']:
	    r = s.delete("https://SUBDOMAIN.zendesk.com/api/v2/users/%s.json" %each["id"])
	    print ("I destroyed User# ") + str(each["id"]) + " " + each["name"]
	if data ['count'] == 0:break
print ("\n\nI'm done destroying")