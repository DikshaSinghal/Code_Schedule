from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import time
import sqlite3
conn=sqlite3.connect('music.sqlite')
cur=conn.cursor()
#conn.execute("CREATE TABLE present11(Website TEXT,Contest_name TEXT,Link TEXT)")
#conn.execute("CREATE TABLE future11(Website TEXT,Contest_name TEXT,Date TEXT,Time TEXT,Link TEXT)")

x = datetime.datetime.now().date()
driver = webdriver.Chrome(executable_path = r'/home/diksha/chromedriver')

driver.get('https://www.codechef.com/contests')

soup = BeautifulSoup(driver.page_source,'lxml')
content = soup.find('div', class_='content-wrapper')
table = content.find_all('table', class_='dataTable')
tr_tags1 = table[0].find_all('tr')
for tr in tr_tags1:
	td_tags = tr.find_all('td')
	i = 0
	for td in td_tags:
		if i == 0:
			i = i + 1
			continue
		elif i == 1:
			#print td.text
			name1 = td.text
			cur.execute("INSERT INTO present11(Website,Contest_name) VALUES (?,?)",("Codechef",name1,))
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
			#print j.text
			name2 = j.text
			if i == 1:
				a = name2
			else:
				b = name2
				cur.execute("INSERT INTO future11(Website,Contest_name,Date,Time) VALUES (?,?,?,?)",("Codechef",a,b[0:11],b[13:21],))
			i = i + 1
		else:
			break

driver = webdriver.Chrome(executable_path = r'/home/diksha/chromedriver')
driver.get('https://www.hackerearth.com/challenges/')

soup = BeautifulSoup(driver.page_source,'lxml')

main = soup.find('div',class_="challenge-container")
present = main.find('div',class_="ongoing challenge-list")
upcoming = main.find('div',class_="upcoming challenge-list")
div1 = upcoming.find_all('div',class_="challenge-card-modern")
div5 = present.find_all('div',class_="challenge-card-modern")
for div in div5:
	div6 = div.find('div',class_="challenge-content align-center")
	div7 = div6.find('div',class_="challenge-name ellipsis dark")
	#print div7.text
	cur.execute("INSERT INTO present11(Website,Contest_name) VALUES (?,?)",("HackerEarth",div7.text,))

div1 = upcoming.find_all('div',class_="challenge-card-modern")
for div in div1:
	div2 = div.find('div',class_="challenge-content align-center")
	div3 = div2.find('div',class_="challenge-name ellipsis dark")
	#print div3.text
	div4 = div2.find('div',class_="date less-margin dark")
	#print div4.text
	cur.execute("INSERT INTO future11(Website,Contest_name,Date,Time) VALUES (?,?,?,?)",("HackerEarth",div3.text,div4.text[0:6],div4.text[8:13],))

driver = webdriver.Chrome(executable_path = r'/home/diksha/chromedriver')
driver.get('https://codeforces.com/contests')

soup = BeautifulSoup(driver.page_source,'lxml')

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
		#print td1[0].text
		a = td1[0].text
		#print td1[2].text
		b = td1[2].text[18:29]
		c = td1[2].text[30:35]
        cur.execute("INSERT INTO future11(Website,Contest_name,Date,Time) VALUES (?,?,?,?)",("Codeforces",a,b,c,))


conn.commit()
cur.execute('SELECT Website,Contest_name FROM present11')
for con in cur:
	print con

conn.commit()
cur.execute('SELECT Website,Contest_name,Date,Time FROM future11')
for con in cur:
	print con
