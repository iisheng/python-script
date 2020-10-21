from requests_html import HTMLSession

BASE_URL = "https://blog.csdn.net/butonce"

session = HTMLSession()

r = session.get(BASE_URL)
titles = r.html.links
print(titles)

for i, title in enumerate(titles):
    if title.find('article/details') >= 0:
        session.get(title)
        print(title)
