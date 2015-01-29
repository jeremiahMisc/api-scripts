'''
Creates a ticket in Zendesk.

@author: pchhetri
'''

print ("\nTICKET MAKER\n\n")
import requests
payload = '{"ticket":{"requester":{"name":"Timmy Tester", "email":"testuser@test.com.ne.nl"}, "subject": "Test API Tikcet", "comment": { "body": "This is a test ticket created via the API. Technically this is all a JSON payload" }}}'
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
for x in range (0,1):
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/tickets.json", data=payload)
	print ("Create ticket #" + str(x))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")
	print r.headers