import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')

except:
    print('NÃO consegui acessar o site')

else:
    print('CONSEGUI acessar o site')