'''
Updates items from a collection using specified ids. The example below
updates tickets with certain ids and sets the satisfaction_rating to good with comment.

@author: pchhetri
'''

print ("\nCOLLECTION UPDATER\n\n")
import requests
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')
payload = '{"satisfaction_rating": {"score": "good", "comment": "Awesome support."}}'
collection = [7680, 7655, 7665] #declare ids you want to update
for x in range (106,207):
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/tickets/" + str(x) + "/satisfaction_rating.json", data=payload)
	print ("Update item #" + str(x))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")