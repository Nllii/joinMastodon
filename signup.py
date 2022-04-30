import re 
import requests
import fakeuser
import pprint
# https://github.com/mastodon/mastodon



temp_email_domain = "@zetmail.com"
def joinMastodon():
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
    response = requests.get('https://api.joinmastodon.org/servers')
    for infomation in response.json():
        domain = infomation['domain']
        description = infomation['description']
        signUp = requests.post('https://'+domain+'/api/v1/apps', headers=headers, json=json_data)
        # print(signUp.json())
        for key in signUp.json():
            if key == 'client_secret':
                auth = signUp.json()[key]
                # print(signUp.json()['client_secret'])
                addy,SSN,phone,phoneprefix,birthday,age,tropicalzodiac,email,username,password,website,useragent,cardtype,card,exp,CVC,company,job,height,weight,bloodtype,UPSTrackingnum,MoneyGram,WesternUnion,favcolor,car,GUID = fakeuser.FakeNameGenerator().GenerateIdenity()
                create_account(username,password,email,domain,auth)
                # {'id': '84117', 'name': 'Mastodon for iOS', 'website': 'https://app.joinmastodon.org/ios', 'redirect_uri': 'mastodon://joinmastodon.org/oauth', 'client_id': 'pxX9Cut_0BOV-hj8sDKdYBuF3fhOJFAYqq4LbqVtLr8', 'client_secret': 'oEED82p5bu62rP26tZqeCsT2IPqNXyeTF1kIzDzFvM0', 'vapid_key': 'BIqC7gExWl9KYi9D89xF2SaYYmEA0BVO8hZizOOEu390mhjFUqfwysW3sEkklpjfIevoVY_2OkIFg8O_pGZGBMA='}











def create_account(username,password,email,domain,auth):
    headers = {
        # 'Content-Length': '123',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer {0}'.format(auth),
    }

    json_data = {
        'email': ''+username+'@zetmail.com',
        'username': username,
        'password': password,
        'reason': '',
        'agreement': True,
        'locale': 'en',
    }

    response = requests.post('https://'+domain+'/api/v1/accounts', headers=headers, json=json_data)
    print(response.json())

        # print(domain, description)

        # pprint.pprint(infomation)
joinMastodon()
    # print(response.text)


#     # return response.json()









addy,SSN,phone,phoneprefix,birthday,age,tropicalzodiac,email,username,password,website,useragent,cardtype,card,exp,CVC,company,job,height,weight,bloodtype,UPSTrackingnum,MoneyGram,WesternUnion,favcolor,car,GUID = fakeuser.FakeNameGenerator().GenerateIdenity()
print(SSN,phone,phoneprefix,username)



