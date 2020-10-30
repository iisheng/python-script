import hashlib
import os.path

filename = '/Users/lisheng/KkbCode/kkb-cloud-config-repo/account-console.yml'
if os.path.isfile(filename):
    fp = open(filename, 'rb')
    contents = fp.read()
    fp.close()
    print(hashlib.md5(contents).hexdigest())
else:
    print('file not exists')
