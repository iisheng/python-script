from requests_html import HTMLSession

BASE_URL = "https://juejin.im/post/6856597850382729223"

session = HTMLSession()

r = session.get(BASE_URL)

print(r.html)

titles = r.html.find('a.title')
for i, title in enumerate(titles):
    print(f'{i + 1} [{title.text}](https://juejin.im{title.attrs["href"]})')
    item = session.get('https://juejin.im' + title.attrs["href"])
