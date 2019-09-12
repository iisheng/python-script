from urllib.request import urlopen

from bs4 import BeautifulSoup

job_url = 'https://kenli.baixing.com/chuguolaowu/a1878099097.html?from=regular'
job_url = urlopen(job_url)

job_soup = BeautifulSoup(job_url)

job_name = job_soup.find('h1')
print(job_name.getText())

company_name = job_soup.find("a", {'class': 'poster-name'})
print(company_name.getText())

salary = job_soup.find("span", {'class': 'price'})
print(salary.getText())

work_address = job_soup.find("div", {'class': 'viewad-meta2-item'})
print(work_address.getText())

contact = job_soup.find("a", {'class': 'contact-no'})
print(contact.getText())

wx = job_soup.find("div", {'class': 'detail'})
print(wx.getText())

descs = job_soup.findAll("div", {'class': 'viewad-text'})

for desc in descs:
	print(desc.getText())

company_cont = job_soup.findAll("div", {'class': 'company-cont'})

for cont in company_cont:
	print(cont.getText())
