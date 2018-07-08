from urllib import parse, request
import json
import hashlib
import hmac
import time
import os
import binascii

secret = b'1234'
data = json.dumps({ "rfid":"000000", 
                    "nonce":binascii.hexlify(os.urandom(10)).decode()+str(int(time.time())), 
                    "timestamp":int(time.time())}).encode('utf8')
headers = {'X-SIGNATURE': hmac.new(secret, data, hashlib.sha512).hexdigest(), 'Content-Type': 'application/json'}



req = request.Request("https://test.agimpel.com/wp-content/plugins/vcs-automat-api/endpoints/auth.php", data = data, headers = headers)

try:
    resp = request.urlopen(req)
    print(resp.read().decode('utf-8'))
    print(resp.code)
except Exception as e:
    print(e)
