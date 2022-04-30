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



def create_accounts():
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
        access_key =token(client_id,client_secret,domain)
        addy,SSN,phone,phoneprefix,birthday,age,tropicalzodiac,email,username,password,website,useragent,cardtype,card,exp,CVC,company,job,height,weight,bloodtype,UPSTrackingnum,MoneyGram,WesternUnion,favcolor,car,GUID  = fakeuser.FakeNameGenerator().GenerateIdenity()
        create_account(access_key,password,email,domain,username)
        with open('accounts.csv', 'a') as f:
            f.write(domain+','+email+','+username+','+password+'\n')
        print(domain,email,username,password)
        continue
        


    






def create_account(access_token,password,email,domain,username):
    headers = {
        
        # 'Content-Length': '134',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer {0}'.format(access_token),
    }

    json_data = {
        'email': email,
        'username': username,
        'password': password,
        'reason': '',
        'agreement': True,
        'locale': 'en',
    }

    response = requests.post('https://'+domain+'/api/v1/accounts', headers=headers, json=json_data)
    print(response.json())

        




create_accounts()