import requests
import fakeuser
import pprint
import random 
import json
from json import JSONDecodeError
# get JSONDecodeError when using this function

domains_list = []
# https://github.com/mastodon/mastodon
temp_email_domain = "@gmail.com"


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


not_allowed_domain= "mstdn.jp","troet.cafe"


def create_accounts():
        response = requests.get('https://api.joinmastodon.org/servers')

        for infomation in response.json():
            domain = infomation['domain']
            print(domain)
            description = infomation['description']
            # init_instance = requests.get('https://'+domain+'/api/v1/instance')
            try:
                init_instance = requests.get('https://'+domain+'/api/v1/instance')
                print(init_instance.json())
                message_ ={
                    'message': 'This domain is not allowed to create account.',
                    'info': init_instance.json()

                }
                print(message_)
                print(domain)
                print("\n")
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
                if domain not in not_allowed_domain:
                    apps = requests.post('https://'+domain+'/api/v1/apps', headers=headers, json=json_data)
                    print(apps.json())
                    print("\n")
                    print("\n")
                else:
                    print(message_)
            except JSONDecodeError or Exception as e:
                print("\n")
                continue

            client_secret =  apps.json()['client_secret']
            client_id  = apps.json()['client_id']
            access_key = token(client_id,client_secret,domain)
            addy,SSN,phone,phoneprefix,birthday,age,tropicalzodiac,email,username,password,website,useragent,cardtype,card,exp,CVC,company,job,height,weight,bloodtype,UPSTrackingnum,MoneyGram,WesternUnion,favcolor,car,GUID  = fakeuser.FakeNameGenerator().GenerateIdenity()
            account_headers = {
                
                # 'Content-Length': '134',
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': 'Bearer {0}'.format(access_key),
            }

            account_data = {
                'email': username+temp_email_domain,
                'username': username,
                'password': password,
                'reason': '',
                'agreement': True,
                'locale': 'en',
            }

            response = requests.post('https://'+domain+'/api/v1/accounts', headers=account_headers, json=account_data)
            # save the response in a csv file
            with open('accounts.csv', 'a') as f:
                f.write('email:'+username+temp_email_domain,'\tpassword:'+password,'\tdomain:'+domain,'username:'+username,'\n')

            print(response.json())

create_accounts()