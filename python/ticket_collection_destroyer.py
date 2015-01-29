'''
Deletes a range of tickets in Zendesk using the /destroy_many.json endpoint that handles up to
100 ticket IDs at a time.

@author: pchhetri
'''

print ("\nTICKET DESTROYER\n\n")
import requests
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
for ticket in range (198,200): #delcare id here
	r = s.delete("https://SUBDOMAIN.zendesk.com/api/v2/tickets/destroy_many.json?ids=" + str(ticket))
	print ("Delete ticket #" + str(ticket))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")