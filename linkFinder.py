from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):


	def __init__(self, baseURL, pageURL):
		super().__init__()
		self.baseURL = baseURL
		self.pageURL = pageURL
		self.links = set()

	def handleStartTag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.baseURL, value)
					self.links.add(url)

	def pageLinks(self):
		return self.links

	def error(self, message):
		pass
