
import requests

#print(page.content)

from bs4 import BeautifulSoup


checkedLinks = list()
external = list()

base = "http://www.cphcs.ca.gov/"

def checkWebsite(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    i = 1
    if soup.find_all('a', href=True) is None:
        return 0
        print("None url: " , url)
    for a in soup.find_all('a', href=True):
        #print(a['href'])
        if (a['href'].startswith("#")) or (a['href'] == '/') or (a['href'].startswith("mailto")) or (a['href'] in checkedLinks):
            continue

        if ("http" in a['href']): #Checks if external link
            if url.split("//",1)[1] not in a['href']:
                if not "www.cphcs.ca.gov" in a['href']:
                    external.append(a['href'])
                    #print(a['href'])
                    continue

        checkedLinks.append(a['href'])
        if "www." not in a['href']:
            #print("www on ", a['href'])
            if url == base:
                a['href'] = base + a['href']
            else:
                if (a['href'].startswith("/")):
                    a['href'] = a['href'][1:]
                print("Url: " , url ,"Original: " , a['href'])
                a['href'] = url.rsplit('/',1)[0] + "/" + a['href']


        if not (a['href'].startswith("http")):
            a['href'] = "http://" + a['href']


        #if "../" in a['href']:
            #a['href'] = "http://www.cphcs.ca.gov/pra.aspx"


        print("Found the URL:", a['href'])
        if not (a['href'].endswith(".pdf") or a['href'].endswith(".xls") or a['href'].endswith(".docx")):
            checkWebsite(a['href'])


checkWebsite("http://www.cphcs.ca.gov/")


print(len(checkedLinks))
