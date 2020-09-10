from urllib.request import urlopen
from html.parser import HTMLParser
from html.entities import name2codepoint

sites = ['https://stackoverflow.com/',
         # 'https://www.computerworld.com/',
         # 'https://habr.com/ru/news/',
         # 'https://www.it-world.ru/it-news/market/',
         ]


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)


for url in sites:
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('utf8')
    total_bytes = len(html_data)
    parser = MyHTMLParser()
    parser.feed(html_data)
