#!$pythonpath
# -*- coding: utf-8 -*-
import os, sys
import subprocess
import json
import hashlib, hmac
from datetime import datetime

hpmanagement_path = "$hpmanagement_path"
sys.path.append(hpmanagement_path)
from webhookconf import secret
webhooklogfilepath = hpmanagement_path + '/webhook.log'
updatelogfilepath = hpmanagement_path + '/update.log' 

os.environ['PATH'] = '$path'

target_branch = ['refs/heads/master']

print('Content-Type:text/html\n\n')

data = sys.stdin.read()
payload = json.loads(data)
signature_name = 'HTTP_X_HUB_SIGNATURE'
if signature_name in os.environ.keys():
    signature = os.environ[signature_name]
else:
    signature = ''

if secret:
    hasher = 'sha1=' + hmac.new(secret, bytes(data, 'utf-8'), hashlib.sha1).hexdigest()
    # print('Signature : {}'.format(signature))
    # print('Calculated: {}'.format(hasher))
    if signature != hasher:
        print('Signature could not be verified.')
        exit()
    else:
        print('Signature verified.')

branch = payload['ref']

f = open(webhooklogfilepath, 'a')
print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()), 'Branch', branch, 'pushed: ', end='', file=f)

if branch in target_branch:
    os.chdir(hpmanagement_path)
    with open(updatelogfilepath, 'a') as uf:
        print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()), file=uf)
        subprocess.call(['sh', 'tools/updatesite.sh', 'Auto-push by hp_management/master update.'],
                        stdout=uf, stderr=uf)
    print('website compiled and (possibly) pushed.', file=f)
else:
    print('nothing done.', file=f)

f.close()
