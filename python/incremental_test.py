import grequests
import requests
import sys
import json
import random
import time
import datetime
import calendar
import csv
import shutil
import codecs
import locale
import io

def main():

    user = '' + '/token'
    token= ''
    subdomain = ''

    # user = '<user>' + '/token'
    # token = '<token>'
    # subdomain = '<subdomain>'

    start_time = datetime.datetime.now() - datetime.timedelta(days = 15)
    time_unix = str(calendar.timegm(start_time.utctimetuple()))

    #uncomment this and comment the next line to instead start from the very beginning
    #next_page = 'https://{1}.zendesk.com/api/v2/exports/tickets.json?start_time={0}'.format(0, subdomain)
    next_page = 'https://{1}.zendesk.com/api/v2/exports/tickets.json?start_time={0}'.format(time_unix, subdomain)

    Ids =[]
    Ids_Error = []

    def write_data(raw_data):
        # with codecs.open('tickets.csv', 'wb') as f:
        #     writer = csv.writer(f)
        writer = csv.writer(sys.stdout)
        writer.writerow([
                    'Id',
                    'Requester',
                    'Requester_id',
                    'Requester_external_id',
                    'Requester_email',
                    'Assignee',
                    'Group',
                    'Subject',
                    'Tags',
                    'Status',
                    'Priority',
                    'Via',
                    'Ticket_type',
                    'Created_at',
                    'Updated_at',
                    'Assigned_at',
                    'Organization',
                    'Due_date',
                    'Initially_assigned_at',
                    'Solved_at',
                    'Satisfaction_Score',
                    'Contact_Reason',
                    'Reservation_ID',
                    'Claim_number',
                    'Outbound',
                    'Audi_Tickets'])

        for result in raw_data:

            # Get mapping via raw_data['field_headers']
            row = []

            Id = result['id']
            row.append(Id)

            Requester = result['req_name']
            row.append(Requester)

            Requester_id = result['req_id']
            row.append(Requester_id)

            Requester_external_id = result['req_external_id']
            row.append(Requester_external_id)

            Requester_email = result['req_email']
            row.append(Requester_email)

            Assignee = result['assignee_name']
            row.append(Assignee)

            Group = result['group_name']
            row.append(Group)

            Subject = result['subject']
            row.append(Subject)

            Tags = result['current_tags']
            row.append(Tags)

            Status = result['status']
            row.append(Status)

            Priority = result['priority']
            row.append(Priority)

            Via = result['via']
            row.append(Via)

            Ticket_type = result['ticket_type']
            row.append(Ticket_type)

            Created_at = result['created_at']
            row.append(Created_at)

            Updated_at = result['updated_at']
            row.append(Updated_at)

            Assigned_at = result['assigned_at']
            row.append(Assigned_at)

            Organization = result['organization_name']
            row.append(Organization)

            Due_date = result['due_date']
            row.append(Due_date)

            Initially_assigned_at = result['initially_assigned_at']
            row.append(Initially_assigned_at)

            Solved_at = result['solved_at']
            row.append(Solved_at)

            Satisfaction_Score = result['satisfaction_score']
            row.append(Satisfaction_Score)

            Contact_Reason = result['field_21157455']
            row.append(Contact_Reason)

            Reservation_ID = result['field_247882']
            row.append(Reservation_ID)

            Claim_number = result['field_20998312']
            row.append(Claim_number)

            Outbound = result['field_20523696']
            row.append(Outbound)

            Audi_Tickets = result['field_20526282']
            row.append(Audi_Tickets)

            try:
                row = [unicode(item).encode('utf8') for item in row]
                if(result['status'] == 'Deleted'):
                    writer.writerow(row)
                    Ids.append(Id)
            except:
                Ids_Error.append(Id)
                pass


    tickets = []
    sanity = 0

    while next_page:
        data = requests.get(next_page, auth=(user, token))

        if data.ok:
            sanity = (sanity - 1) if (sanity > 1) else sanity
            data = data.json()
            tickets.extend(data['results'])
            new_page = data.get('next_page')
            newTime = int(new_page.split('=')[-1])
            now = time.mktime(datetime.datetime.now().timetuple())
            print((now - newTime)/3600)

            if new_page != next_page and now - newTime > 300:
                next_page = new_page
                time.sleep(60)
            else:
                break
        elif data.status_code == 429:
            sanity += 1
            if(sanity > 5):
                print('Too many retries')
                break
            retry = data.headers['Retry-After']
            print('429 Error, Retrying after {0} seconds.'.format(retry))
            time.sleep(float(retry) * sanity)
        else:
            print(data.status_code)
            sanity += 1
            if(sanity > 5):
                print('Too many retries')
                break
            time.sleep(60 * sanity)

    print('-------------------CSV_DATA-------------------')
    write_data(tickets)
    print('-------------------TICKET_IDS-------------------')
    print(Ids)
    print('-------------------TICKET_ERRORS-------------------')
    print(Ids_Error)
    print('-------------------STATISTICS-------------------')
    print('{0} / {1}'.format(len(Ids), len(Ids_Error)))



if __name__ == '__main__':
    main()
