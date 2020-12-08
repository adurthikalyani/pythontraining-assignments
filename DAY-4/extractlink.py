import re

links=[]

text_file= open('linksfile.txt', 'r')
File = text_file.read()
links = re.findall("(https?://[^\s]+)", File)

for link in links:
    print(link)
