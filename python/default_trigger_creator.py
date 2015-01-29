'''
Imports the default Zendesk Triggers into the specified account

@author: pchhetri
'''

print ("\nZendesk Default TRIGGER MAKER\n\n")
import requests
payload1 = '{"trigger":{"title":"Notify requester of received request","active":true,"actions":[{"field":"notification_user","value":["requester_id","Request received: {{ticket.title}}","Your request ({{ticket.id}}) has been received and is being reviewed by our support staff.\\n\\nTo add additional comments, reply to this email.\\n<br>{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"update_type","operator":"is","value":"Create"},{"field":"status","operator":"is_not","value":"solved"}],"any":[]},"position":0}'
payload2 = '{"trigger":{"title":"Notify requester of comment update","active":true,"actions":[{"field":"notification_user","value":["requester_id","[{{ticket.account}}] Re: {{ticket.title}}","Your request ({{ticket.id}}) has been updated. To add additional comments, reply to this email.\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"update_type","operator":"is","value":"Change"},{"field":"comment_is_public","operator":"is","value":"requester_can_see_comment"},{"field":"requester_id","operator":"is_not","value":"current_user"},{"field":"status","operator":"not_value","value":"solved"}],"any":[]},"position":1}'
payload3 = '{"trigger":{"title":"Notify requester of solved request","active":true,"actions":[{"field":"notification_user","value":["requester_id","[{{ticket.account}}] Re: {{ticket.title}}","Your request ({{ticket.id}}) has been solved. To reopen this request, reply to this email.\\n<br>{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"status","operator":"value","value":"solved"},{"field":"comment_is_public","operator":"is","value":"requester_can_see_comment"}],"any":[]},"position":2}'
payload4 = '{"trigger":{"title":"Notify assignee of comment update","active":true,"actions":[{"field":"notification_user","value":["assignee_id","[{{ticket.account}}] Re: {{ticket.title}}","This ticket (#{{ticket.id}}) has been updated.\\n\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"comment_is_public","operator":"is","value":"not_relevant"},{"field":"assignee_id","operator":"is_not","value":"current_user"},{"field":"assignee_id","operator":"is_not","value":"requester_id"},{"field":"assignee_id","operator":"not_changed","value":null},{"field":"status","operator":"not_value_previous","value":"solved"}],"any":[]},"position":4}'
payload5 = '{"trigger":{"title":"Notify assignee of assignment","active":true,"actions":[{"field":"notification_user","value":["assignee_id","[{{ticket.account}}] Assignment: {{ticket.title}}","You have been assigned to this ticket (#{{ticket.id}}).\\n\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"assignee_id","operator":"changed","value":null},{"field":"assignee_id","operator":"is_not","value":"current_user"}],"any":[]},"position":5}'
payload6 = '{"trigger":{"title":"Notify assignee of reopened ticket","active":true,"actions":[{"field":"notification_user","value":["assignee_id","[{{ticket.account}}] Re: {{ticket.title}}","This ticket (#{{ticket.id}}) has been reopened.\\n\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"assignee_id","operator":"is_not","value":"current_user"},{"field":"status","operator":"value_previous","value":"solved"},{"field":"status","operator":"is_not","value":"closed"}],"any":[]},"position":6}'
payload7 = '{"trigger":{"title":"Notify group of assignment","active":true,"actions":[{"field":"notification_group","value":["group_id","[{{ticket.account}}] \\"{{ticket.group.name}}\\" assignment:  {{ticket.title}}","This ticket (#{{ticket.id}}) has been assigned to group \'{{ticket.group.name}}\', of which you are a member.\\n\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"group_id","operator":"changed","value":""},{"field":"group_id","operator":"is_not","value":""},{"field":"assignee_id","operator":"is","value":""}],"any":[]},"position":7}'
payload8 = '{"trigger":{"title":"Notify all agents of received request","active":true,"actions":[{"field":"notification_user","value":["all_agents","[{{ticket.account}}] {{ticket.title}}","A ticket (#{{ticket.id}}) by {{ticket.requester.name}} has been received. It is unassigned.\\n\\n{{ticket.comments_formatted}}"]}],"conditions":{"all":[{"field":"update_type","operator":"is","value":"Create"},{"field":"group_id","operator":"is","value":""}],"any":[]},"position":8}'
payload9 = '{"trigger":{"title":"Auto-assign to first email responding agent","active":false,"actions":[{"field":"assignee_id","value":"current_user"}],"conditions":{"all":[{"field":"update_type","operator":"is","value":"Change"},{"field":"current_via_id","operator":"is","value":"4"},{"field":"assignee_id","operator":"is","value":""},{"field":"role","operator":"is_not","value":"end_user"}],"any":[]},"position":9998}'
payload = [payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9]
number = -1
s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
s.auth = ('USR', 'PASS')
collection = ['(1) Notify requester of received request', '(2) Notify requester of comment update', '(3) Notify requester of solved request', '(4) Notify assignee of comment update', '(5) Notify assignee of assignment', '(6) Notify assignee of reopened ticket', '(7) Notify group of assignment', '(8) Notify all agents of received request', '(9) Auto-assign to first email responding agent']
for x in collection:
	number += 1
	r = s.post("https://SUBDOMAIN.zendesk.com/api/v2/triggers.json", data=payload[number])
	print ("Create trigger "+ str(x))
	i = r.status_code
	print ("Status Code: " + str(i) + "\n")
	print r.headers
	print "\n\n"