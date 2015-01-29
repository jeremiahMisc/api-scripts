'''
Creates Zendesk tickets pulling in the top news articles from USA Today

@author: pchhetri
'''

print ("\n\nTHE DYNAMIC TICKET MAKER\n\n")
import requests
import json
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR','PASS')

r = requests.get ("http://api.usatoday.com/open/articles/topnews/home?encoding=json&api_key=yap33mq57zy7rst4h94y9389")
data = json.loads(r.text)
for each in data['stories']:
	payload = '{"ticket":{"requester":{"name":"Joe Schmoe", "email":"testuser@example.com.ne"}, "subject":"%s", "comment": { "body": "%s" }}}' %(each["title"],each["description"])
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/imports/tickets.json", data=payload)
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")

