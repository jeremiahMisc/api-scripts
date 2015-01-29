'''
Creates 100 tickets in Zendesk.

@author: pchhetri
'''

print ("\n\nMANY TICKET MAKER\n\n")
import requests
payload = '{"ticket":{"requester":{"name":"Joe Schmoe", "email":"joeschmoe@example.com.uk.ne"}, "subject":"My printer is on fire!", "comment": { "body": "The smoke is very colorful." },"status":"solved"}}'
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
for x in range (0,100): #declare number of tickets that you want to create
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/imports/tickets.json", data=payload)
	print ("Created ticket #" + str(x) )
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")