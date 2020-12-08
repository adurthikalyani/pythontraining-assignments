import re

class links:
    def __init__(myObj, usernames, httplink, durations):
        myObj.usernames = usernames
        myObj.httplink = httplink
        myObj.durations = durations

urls = []
names = []
duration = []
text_file= open('linksfile.txt', 'r')
File = text_file.read()
urls = re.findall("(https?://[^\s]+)", File)
names = re.findall("(?<=from )(.*)(?=to)", File)
duration = re.findall("[0-1][0-2]:[0-5][0-9] AM|[0-1][0-2]:[0-5][0-9] PM", File)

list_links = []

for (valuea,valueb,valuec) in zip(names, urls, duration):
    l = links(valuea,valueb,valuec)
    list_links.append(l)

for link in list_links:
    print(f'Link: {link.httplink} --- Sent By: {link.usernames} --- At:  {link.durations}')