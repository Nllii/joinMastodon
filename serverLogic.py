import requests
import fakeuser
import pprint
import random 

# https://github.com/mastodon/mastodon
# temp_email_domain = "@zetmail.com"


def token(client_id,client_secret,domain):
   
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        # 'Content-Length': '242',
    }

    json_data = {
        'client_id': client_id,
        'scope': 'read write follow push',
        'redirect_uri': 'mastodon://joinmastodon.org/oauth',
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }

    response = requests.post('https://'+domain+'/oauth/token', headers=headers, json=json_data).json()
    access_token = response['access_token']
    return access_token
    # print(response.json())



def servers():
    response = requests.get('https://api.joinmastodon.org/servers')
    for infomation in response.json():
        domain = infomation['domain']
        description = infomation['description']
        init_instance = requests.get('https://'+domain+'/api/v1/instance')
        # print(init_instance.json())
        # print(domain,description)
        # return domain,description
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            # 'Content-Length': '171',
        }

        json_data = {
            'redirect_uris': 'mastodon://joinmastodon.org/oauth',
            'website': 'https://app.joinmastodon.org/ios',
            'client_name': 'Mastodon for iOS',
            'scopes': 'read write follow push',
        }

        apps = requests.post('https://'+domain+'/api/v1/apps', headers=headers, json=json_data).json()
        client_secret = apps['client_secret']
        client_id  = apps['client_id']
        token(client_id,client_secret,domain)


    
