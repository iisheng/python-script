# 循环 获取百姓网 出国劳务列表
# 获取列表中 每一个 岗位的详细url
# 爬取岗位详情 详细信息 包括岗位基本信息和 公司基本信息
# 将拿到的数据 导出到 excel 中

import time
from urllib.request import urlopen

import records
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/lisheng/software/chromedriver')

rows = [

]


class JobInfo:
	def __init__(self, job_name, company_name, salary, work_address, contact, wx, job_desc, job_company_content):
		self.job_name = job_name
		self.company_name = company_name
		self.salary = salary
		self.work_address = work_address
		self.contact = contact
		self.wx = wx
		self.job_desc = job_desc
		self.job_company_content = job_company_content


def convert_to_dict(obj):
	# 把Object对象转换成Dict对象
	dict = {}
	dict.update(obj.__dict__)
	return dict


def craw_job_detail(job_url):
	# driver.get(job_url)
	# driver.maximize_window()
	# driver.find_element_by_class_name('show-contact').click()
	# content = driver.page_source.encode('utf-8')
	# driver.close()
	content = urlopen(job_url)
	soup = BeautifulSoup(content, 'lxml')
	return soup


def parse_web_page(job_soup):
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
	wx_cont = ''
	if wx:
		wx_cont = wx.getText()
	print(wx_cont)

	descriptions = job_soup.findAll("div", {'class': 'viewad-text'})

	job_desc = ''
	for desc in descriptions:
		print(desc.getText())
		job_desc = job_desc + desc.getText()

	company_introduce = job_soup.find("div", {'class': 'viewad-text'})
	print('公司介绍', company_introduce.getText())

	company_cont = job_soup.findAll("div", {'class': 'company-cont'})

	job_company_content = ''

	for cont in company_cont:
		print(cont.getText())
		job_company_content = job_company_content + cont.getText()

	job_info = JobInfo(job_name.getText(), company_name.getText(), salary.getText(), work_address.getText(),
					   contact.getText(), wx_cont, job_desc, job_company_content)

	rows.append(convert_to_dict(job_info))


url = 'https://china.baixing.com/chuguolaowu/'

driver.get(url)

driver.maximize_window()

time.sleep(20)

# driver.find_element_by_class_name('show-contact').click()
content = driver.page_source.encode('utf-8')

driver.close()
soup = BeautifulSoup(content, 'lxml')

name_list = soup.find_all("a", {'class': 'ad-title'})

for name in name_list:
	try:
		url_detail = craw_job_detail(name.get("href"))
		print('URL 详情: ', url_detail)
		parse_web_page(url_detail)  # get_text()函数剔除字符串中所有tag符号只保留tag中包含的文本
		break
	except Exception as e:
		print(e)

results = records.RecordCollection(iter(rows))
with open('demo.xlsx', 'wb') as f:
	f.write(results.export('xlsx'))
