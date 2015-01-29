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


def csv_writer(topics):
    with open('topics.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([
                    'topic_category',
                    'topic_forum',
                    'topic_title',
                    'topic_last_updated',
                    'comment_author',
                    'comment_last_updated',
                    'file_name',
                    'download_url'])
        for topic in topics:
            for comment in topic['comments']:
                for attachment in comment['attachments']:
                    forum = None if not topic['forum'] else topic['forum']['name']
                    category = (None if not forum else
                               (None if not topic['forum']['category'] else 
                                topic['forum']['category']['name']))
                    title = topic['title']
                    topic_date = topic['updated_at']
                    comment_author = comment['user']['name']
                    comment_date = comment['updated_at']
                    file_name = attachment['file_name']
                    url = attachment['content_url']
                    writer.writerow([category,
                                    forum,
                                    title,
                                    topic_date,
                                    comment_author,
                                    comment_date,
                                    file_name,
                                    url])
def url_writer(topics):
    with open('attachment_urls.txt', 'w') as f:
        for topic in topics:
            for comment in topic['comments']:
                for attachment in comment['attachments']:
                    f.write(attachment['content_url'] + '\n')

def main():
    user = ''
    token=''
    subdomain = ''
    session = Session(subdomain, user, token=token)

    topics = session.get_all('topics.json',
                            params='include=forums', 
                            members=['topics', 'forums'])
    forums = topics['forums']
    for forum_id, forum in forums.items():
        category_id = forum['category_id']
        category = None if not category_id else session.get(
                            'categories/{0}.json'.format(forum['category_id'])
                            ).json()['category']
        forum['category'] = category
    topics = [topic for topic_id, topic in topics['topics'].items()]
    current_topic = 0
    total_topics = len(topics)
    comment_count = 0
    for topic in topics:
        current_topic += 1
        if topic['comments_count'] > 0:
            comments = session.get_all(
                    'topics/{0}/comments.json'.format(topic['id']), 
                    members=['topic_comments', 'users'],
                    params='include=users')
            users = comments['users']
            comments = [comment for comment_id, comment in comments['topic_comments'].items()]
            for comment in comments:
                comment['user'] = users[comment['user_id']]
            comment_count += len(comments)
            topic['comments'] = comments
        else:
            topic['comments'] = []
        print('Topic: {} / {}, {:.2%} done, {} comments - {} total'.format(current_topic, 
                                                                   total_topics, 
                                                                   current_topic/total_topics, 
                                                                   topic['comments_count'],
                                                                   comment_count))
        topic['forum'] = forums[topic['forum_id']]
    csv_writer(topics)
    url_writer(topics)

if __name__ == '__main__':
    main()
