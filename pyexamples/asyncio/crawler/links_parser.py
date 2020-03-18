from html.parser import HTMLParser
import urllib


class LinksParser(HTMLParser):

  def __init__(self, base, seen):
    super().__init__()
    self.base = base
    self.links = []
    self.seen = seen

  def error(self, message):
    print("[LinksParser:error] got error:\n", message)
    pass

  # This is a function that HTMLParser normally has
  # but we are adding some functionality to it
  def handle_starttag(self, tag, attrs):
    # we are looking for the beginning of a link. Links normally look
    # like <a href="www.someurl.com"></a>
      if tag == 'a':
        for (key, value) in attrs:
          #print("parser: found key = ", key)
          if key == 'href':
            #print("parser: found value = ", value)
            # We are grabbing the new URL. We are also adding the
            # base URL to it. For example:
            # www.somewhere.com is the base and
            # somepage.html is the new URL (a relative URL)
            #
            # We combine a relative URL with the base URL to create
            # an absolute URL like:
            # www.somewhere.com/somepage.html
            # newUrl = ''
            # if value.startswith('https://') or value.startswith('http://'):
            #   newUrl = value
            # else:
            #   newUrl = urllib.parse.urljoin(self.base, value)

            new_url = urllib.parse.urljoin(self.base, value)
            if not new_url in self.seen:
              self.seen.add(new_url)
              print('LinksParser: base=', self.base, ', newUrl =', new_url)
              self.links = self.links + [new_url]

  def parse(self, html: str):
    self.feed(html)
    #print('parse: return after feed:', self.links)
    return self.links
