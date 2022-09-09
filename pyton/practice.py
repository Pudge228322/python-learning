import os
import time

sayt = input()

if 'https://' in sayt:
    os.system('start ' + sayt)
    print('if')

elif 'www.' in sayt:
    os.system('start ' + sayt)
    print('elif')

else:
    sayt = 'https://www.' + sayt
    os.system('start ' + sayt)
    print('else')

time.sleep(5)


