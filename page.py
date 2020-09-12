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


class PageSizer:
    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        html_data = html_data.decode('utf8')
        self.total_bytes += len(html_data)
        extractor = LinkExtractor()
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            self.total_bytes += len(extra_data)

    def _get_html(self, url):
        res = urlopen(url)
        return res.read()


for links in sites:
    print(f'Go {links}...')
    sizer = PageSizer(url=links)
    sizer.run()
    print(f'For url {links} need download {sizer.total_bytes// 1024} Kb')




