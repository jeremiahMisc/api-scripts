'''
Finds users in Zendesk that have multiple email addresses, prints the user IDs

@author: pchhetri
'''

print ("\n\nFIND USERS WITH MULTIPLE EMAILS\n\n")

import requests
import json
s = requests.Session()
s.auth = ('USR','PASS')

pageNum = 1
nextPage = ""
userIDList = []

while nextPage != None:
	# print pageNum
	r = s.get("https://{SUBDOMAIN}.zendesk.com/api/v2/users.json?page=%s" %pageNum)
	# print r
	data = json.loads(r.text)
	nextPage = data['next_page']
	for each in data['users']:
			userIDList.append(each['id'])
    			# print each['id']
	pageNum+=1
	# print nextPage

print ("You have this many users: " + str(len(userIDList)))

for item in userIDList:
	print item
        q = s.get("https://{SUBDOMAIN}.zendesk.com/api/v2/users/%s/identities.json" %item)
        userIdentities = json.loads(q.text)
        if len(userIdentities['identities']) > 1:
        	for item in userIdentities['identities']:
        		if item['type'] == "email" and item['primary'] == False:
        			print item


print ("\n\nI'm done finding")