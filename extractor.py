from html.parser import HTMLParser


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