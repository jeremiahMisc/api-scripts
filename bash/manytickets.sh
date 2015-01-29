#!/bin/bash

# Creates N number of tickets in a Zendesk
# Don't forget to set the subdomain and Zendesk credentials

if [ $# != 1 ]; then
  echo "Usage: ./manytickets.sh [number of tickets]"
  exit 1
fi

SUBDOMAIN=<subdomain>
ZD_CREDS=<email/token:apikey>
NO_TICKETS=${1}
TICKET_LOG=created_tickets_`date +'%Y-%m-%d_%H-%M'`.log

for (( t=1; t<=${NO_TICKETS}; t++ ))
do
  echo "Creating ticket ${t}"
  curl https://${SUBDOMAIN}.zendesk.com/api/v2/tickets.json \
    -d '{"ticket":{"subject":"My printer is on fire!", "comment": { "body": "The smoke is very colorful." }, "type":"incident"}}' \
    -H "Content-Type: application/json" -u ${ZD_CREDS} -X POST >> ${TICKET_LOG}
done

printf "\nTickets created. See ${TICKET_LOG}\n"
