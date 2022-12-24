import requests
import hashlib
import time

def md5(a):
    return(hashlib.md5(a.encode(encoding='UTF-8')).hexdigest())

timetemp = str(int(time.time()))
params = {
    'token':md5(md5(timetemp)),
    'time':timetemp,
    }

def output(a):
    temp1 = requests.get(url = 'https://ited.ml/60s.php',params=a)
    if temp1.text == 'ok':
        return('ok')
    elif temp1.text == 'token error':
        return(f'token error \n token:\n{params}')
    else:
        return(f'unknow error\nited.ml return:\n{temp1}')
print("网站新闻状态     ",output(params))