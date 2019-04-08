from django.shortcuts import render
import requests as re
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
import os
from .models import Contests

def index(request):
     scrape()
     web = Contests.objects.all()
     dict = {'contests':web}
     return render(request,'firstapp/index.html',context=dict)

def scrape():
    Contests.objects.all().delete()
    content=re.get('https://www.codechef.com/contests').content
    soup = BeautifulSoup(content,'html.parser')
    content = soup.find('div', class_='content-wrapper')
    table = content.find_all('table', class_='dataTable')
    tr_tags1 = table[0].find_all('tr')
    for tr in tr_tags1:
        td_tags = tr.find_all('td')
        i = 0
        for j in td_tags:
            if i == 0:
                i = i + 1
                continue
            elif i == 1 or i == 2:
                name2 = j.text
                if i == 1:
                    an=name2
                    a=j.find('a')
                    l = a['href']
                else:
                    b=name2
                    #print(a)
                    #print(b[0:11])
                    #print(b[13:21])
                    #print(l)
                    new = Contests()
                    new.Website = "Codechef"
                    new.contestname = an
                    new.date = b[0:11]
                    new.time = b[13:21]
                    new.link = "https://www.codechef.com/".strip()+l
                    new.save()
                i = i + 1
            else:
            	break;
    tr_tags2 = table[1].find_all('tr')
    for tr in tr_tags2:
    	td_tags = tr.find_all('td')
    	i = 0;
    	for j in td_tags:
            if i == 0:
            	i = i + 1
            	continue
            elif i == 1 or i == 2:
                name2 =j.text
                if i == 1:
                    an = name2
                    a = j.find('a')
                    l = a['href']
                else:
                    b = name2
                    #print(a)
                    #print(b[0:11])
                    #print(b[13:21])
                    #print(l)
                    new = Contests()
                    new.Website = "Codechef"
                    new.contestname = an
                    new.date = b[0:11]
                    new.time = b[13:21]
                    new.link = "https://www.codechef.com/".strip()+l
                    new.save()
                i = i + 1
            else:
            	break
    content=re.get('https://codeforces.com/contests').content
    soup = BeautifulSoup(content,'html.parser')
    present = soup.find('div',id="pageContent")
    present = soup.find('div',id="pageContent")
    main = present.find('div',class_="contestList")
    final = main.find('div',class_="datatable")
    table1 = final.find('table')
    tr_tags = table1.find_all('tr')
    i = 0
    for tr in tr_tags:
        if i == 0:
        	i = i + 1
        	continue
        else:
            td1 = tr.find_all('td')
            a = td1[2].find('a')
            l = a['href']
            new = Contests()
            new.Website = "Codeforces"
            new.contestname = td1[0].text
            new.date = td1[2].text[0:13]
            new.time = td1[2].text[14:21].strip()+":00"
            new.link = l

            new.save()
