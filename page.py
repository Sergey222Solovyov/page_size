from urllib.request import urlopen

from extractor import LinkExtractor
from utils import time_track

sites = ['https://stackoverflow.com/',
         'https://www.khanacademy.org/',
         'https://habr.com/ru/news/',
         'https://twitter.com/',
         ]


class PageSizer:
    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        html_data = html_data.decode('utf8')
        self.total_bytes +=\
            len(html_data)
        extractor = LinkExtractor()
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            self.total_bytes += len(extra_data)

    def _get_html(self, url):
        print(f'Go {url}...')
        res = urlopen(url)
        return res.read()


@time_track
def main():
    sizers = [PageSizer(url=links) for links in sites]

    for sizer in sizers:
        sizer.run()
    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.total_bytes // 1024} Kb')


if __name__ == '__main__':
    main()
