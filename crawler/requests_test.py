from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.jianshu.com/u/18d731821bfc')
r.html.render(scrolldown=50, sleep=.2)
titles = r.html.find('a.title')
for i, title in enumerate(titles):
    print(f'{i + 1} [{title.text}](https://www.jianshu.com{title.attrs["href"]})')
