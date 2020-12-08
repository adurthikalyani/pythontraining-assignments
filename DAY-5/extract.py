import re

urls = []
text_file= open('file.html', 'r')
File = text_file.read()
urls = re.findall("(https?://[^\s]+)", File)


for link in urls:
    print(link)