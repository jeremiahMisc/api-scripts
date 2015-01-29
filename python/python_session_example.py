from __future__ import division
import requests
import json
import grequests
import csv


class Session:

    def __init__(self, subdomain, user, password = '', token = ''):
        self.subdomain = subdomain
        self.user = user
        if password and not token:
            self.password = password
        if token:
            self.password = token
            self.user = user + '/token'

    def create_url(self, endpoint, params = None, page = 1):
        param_string = params or []
        param_string = param_string if type(param_string) is list else [param_string]
        param_string.append('page={0}'.format(page))
        param_string = '&'.join(param_string)
        url = 'https://{0}.zendesk.com/api/v2/{1}?{2}'.format(self.subdomain, endpoint, param_string)
        return url

    def unwrap_members(self, data, members, paged = False):
        if not members:
            return data
        results = {members: {}} if type(members) is not list else \
                  {member: {} for member in members}
        def create_results(page):
            for key, value in results.items():
                for item in page[key]:
                    value[item['id']] = item
        if not paged:
            create_results(data)
            return results
        for page in data:
            create_results(page)
        return results if len(results) > 1 else results[members]

    def get(self, endpoint, params = None, members = None, page = 1):
        url = self.create_url(endpoint, params, page)
        response = requests.get(url, auth=(self.user, self.password))
        return self.unwrap_members(responses.json(), members)

    def get_all(self, endpoint, params = None, members = None):
        first_page = self.get(endpoint, params)
        count = first_page.json()['count']
        page_slop = 0 if count % 100 == 0 else 1
        page_count = count//100 + page_slop
        print('endpoint: {}, {} elements in {} pages'.format(endpoint, count, page_count))
        user_requests = [grequests.get(self.create_url(endpoint, params, page),
                                       stream=False,
                                       auth=(self.user, self.password))
                        for page in range(2, page_count+1)]
        user_requests = grequests.map(user_requests) or []
        user_requests.append(first_page)
        map(lambda page: page.json(), user_requests)
        return self.unwrap_members(user_requests, members, paged = True)

    def post(self, endpoint, data, user = None):
        if not user:
            user = self.user
        url = self.create_url(endpoint)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, json.dumps(data), auth=(user, self.password), headers=headers)
        return response

    def put(self, endpoint, data, user = None):
        if not user:
            user = self.user
        url = self.create_url(endpoint)
        headers = {'content-type': 'application/json'}
        response = requests.put(url, json.dumps(data), auth=(user, self.password), headers=headers)
        return response


def main():
    user = ''
    token=''
    subdomain = ''
    session = Session(subdomain, user, token=token)

    topics = session.get_all('topics.json',
                            params='include=forums',
                            members=['topics', 'forums'])

if __name__ == '__main__':
    main()
