print('============== isdir bug ===============')

import os.path
import time
import sys
from jnius import autoclass
from android.permissions import request_permissions, Permission, check_permission

request_permissions([Permission.READ_EXTERNAL_STORAGE,
                     Permission.WRITE_EXTERNAL_STORAGE])

for i in range(10):
    print('checking permission, i =', i)
    if check_permission(Permission.WRITE_EXTERNAL_STORAGE):
        print('OK!')
        break
    time.sleep(1)
else:
    print('NO PERMISSION :(')
    sys.exit(1)


Environment = autoclass('android.os.Environment')
storage = Environment.getExternalStorageDirectory().getPath()
print('getExternalStorageDirectory():', storage)  # '/storage/emulated/0' on my machine

mydir = storage + '/foobar'
print('os.mkdir', mydir)
try:
    os.mkdir(mydir)
except OSError as e:
    print(e)
else:
    print('OK')

def check(p):
    import os.path
    print(p)
    print('    isdir():', os.path.isdir(p))
    print('    listdir():', end='')
    try:
        print(os.listdir(p))
    except OSError as e:
        print(e)
    print()

check('/')
check('/storage/')
check('/storage/emulated/')
check('/storage/emulated/0/')
check('/storage/emulated/0/foobar/')

print('============== end isdir bug ===============')

sys.exit(1)
