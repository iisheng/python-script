from requests_html import HTMLSession

session = HTMLSession()
url = 'https://cpppatterns.com/patterns/copy-range-of-elements.html'
r = session.get(url)


def get(title):
	r_title = r.html.find(title)
	r_code = r.html.find('tr > td:nth-child(2) > code > span')  #

	data = []

	print(r_title[0].text)
	for result in r_code:
		data.append(result.text)
		data = " ".join(data)
		print(data)
		data = []


if __name__ == "__main__":
	sel_title = 'head > title'
	get(sel_title)
