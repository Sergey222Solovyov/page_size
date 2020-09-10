from urllib.request import urlopen
from html.parser import HTMLParser
from html.entities import name2codepoint

sites = ['https://stackoverflow.com/',
         'https://www.khanacademy.org/',
         'https://habr.com/ru/news/',
         'https://twitter.com/',
         ]


class LinkExtractor(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('link', 'script'):
            return

        # print("Start tag:", tag)

        attrs = dict(attrs)
        if 'rel' in attrs and attrs['rel'] == 'stylesheet':
            self.links.append(attrs['href'])
        elif 'src' in attrs:
            self.links.append(attrs['src'])

        # for attr in attrs:
        #     print("     attr:", attr)


for url in sites:
    print(f'Go {url}...')
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('utf8')
    total_bytes = len(html_data)
    extractor = LinkExtractor()
    extractor.feed(html_data)
    print(extractor.links)
    for link in extractor.links:
        print(f'\tGo {link}...')
        res = urlopen(link)
        extra_data = res.read()
        total_bytes += len(extra_data)
    print(f'For url {url} need download {total_bytes // 1024} Kb')
