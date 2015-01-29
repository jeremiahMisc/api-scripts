'''
Creates tickets in Zendesk until its stopped using the ticket import endpoint.

@author: pchhetri
'''

print ("\n\nINFINITE TICKET MAKER\n\n")
import requests
payload = '{"ticket":{"requester":{"name":"Joe Schmoe", "email":"testuser@example.com.ne"}, "subject":"My chakra is broken!", "comment": { "body": "Help me be Zen again!" }}}'
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
n = 0
while 1:
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/imports/tickets.json", data=payload)
	n+=1
	print ("Created ticket #" + str(n) )
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")