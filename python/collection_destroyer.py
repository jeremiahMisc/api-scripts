'''
Deletes items from a collection using specified ids. The example below
deletes ticket forms using the ids provided in the collection variable.

@author: pchhetri
'''

print ("\nCOLLECTION DESTROYER\n\n")
import requests
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
collection = ['7680', '7655', '7665'] #declare ids here
for x in collection:
	r = s.delete("https://SUBDOMAIN.zendesk.com/api/v2/ticket_forms/" + str(x) + ".json")
	print ("Delete item #" + str(x))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")