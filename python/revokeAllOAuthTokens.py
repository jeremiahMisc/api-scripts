'''
Revokes all OAuth tokens from an instance of Zendesk.

@author: jeremiahcurrier
'''

print ("\n\nBulk OAuth Token Revocation initiated...\n\n")
import requests
import json
s = requests.Session()
s.auth = ('USR','PASS') # Replace 'USR' & 'PASS' - email/password & email/token:token both work
while 1:
  r = s.get("https://SUBDOMAIN.zendesk.com/api/v2/oauth/tokens.json") # Replace 'SUBDOMAIN'
  data = json.loads(r.text)
  for each in data['tokens']:
      r = s.delete("https://SUBDOMAIN.zendesk.com/api/v2/oauth/tokens/%s.json" %each["id"]) # Replace 'SUBDOMAIN'
      print ("Revoked OAuth Token ID: ") + str(each["id"])
  if data ['count'] == 0:break
print ("\n\nBulk OAuth Token Revocation FINISHED")