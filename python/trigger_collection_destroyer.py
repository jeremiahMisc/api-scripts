'''
Deletes triggers in Zendesk using a range of id
range (31807260,31807261) will delete all triggers that have an id between 31807260 & 31807261

@author: pchhetri
'''

print ("\nTRIGGERs DESTROYER\n\n")
import requests
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
for x in range (31807260,31807261): #declare trigger id here
	r = s.delete("https://SUBDOMAIN.zendesk.com/api/v2/triggers/" + str(x) + ".json")
	print ("Delete Trigger " + str(x))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")