'''
Creates a ticket in Zendesk. Prompting user in terminal for information.

@author: pchhetri
'''

print ("\nSIMPLE TICKET MAKER\n\n")

print ("\nACCCOUNT INFORMATION\n")

SUBDOMAIN = raw_input("Subdomain: ")
USER = raw_input("Email Address: ")
PASSWORD = raw_input("Password: ")

print ("\nTICKET INFORMATION\n")

NAME = raw_input("Requester Name: ")
EMAIl = raw_input("Requester Email: ")
SUBJECT = raw_input("Ticket Subject: ")
DESCRIPTION = raw_input("Ticket Description: ")

import requests
payload = '{"ticket":{"requester":{"name":"%s", "email":"%s"}, "subject": "%s", "comment": { "body": "%s" }}}' %(NAME, EMAIl, SUBJECT, DESCRIPTION)
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('%s' %(USER),'%s' %(PASSWORD))
for x in range (0,1):
	r = s.post("https://" + SUBDOMAIN + ".zendesk.com/api/v2/tickets.json", data=payload)
	print ("\nCreated ticket #" + str(x))
	i = r.status_code
	print ("\n\nStatus Code: " + str(i) + "\n")
	print r.headers