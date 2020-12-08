import urllib.request
import re

link=urllib.request.urlopen('http://ramakrishnavivekananda.info/')
file=link.read()
Data = file.decode('utf-8')

text=re.sub('<.*?>','',Data)
with open('DAY-5/file.txt','w',encoding='utf-8') as file_write:
    file_write.write(text)