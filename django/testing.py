from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path = r'/home/diksha/chromedriver')
driver.get('https://www.hackerearth.com/challenges/')

soup = BeautifulSoup(driver.page_source,'lxml')

main = soup.find('div',class_="challenge-container")
present = main.find('div',class_="ongoing challenge-list")
upcoming = main.find('div',class_="upcoming challenge-list")

div5 = present.find_all('div')
for div in div5:
	div6 = div.find('div',class_="challenge-content align-center")
	div7 = div6.find('div',class_="challenge-name ellipsis dark")
	print div7.text

div1 = upcoming.find_all('div',class_="challenge-card-modern")
for div in div1:
	div2 = div.find('div',class_="challenge-content align-center")
	div3 = div2.find('div',class_="challenge-name ellipsis dark")
	print div3.text
	div4 = div2.find('div',class_="date less-margin dark")
	print div4.text[0:6]
	print div4.text[8:13]
