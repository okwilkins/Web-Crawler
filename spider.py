from urllib.request import urlopen
from linkFinder import LinkFinder
from general import *

class Spider:

	# Class variables (shared amond all instances)
	projectName = ''
	baseURL = ''
	domainName = ''
	queueFile = ''
	crawledFile = ''
	queueSet = set()
	crawledSet = set()

	def __init__(self, projectName, baseURL, domainName):
		Spider.projectName = projectName
		Spider.baseURL = baseURL
		Spider.domainName = domainName
		Spider.queueFile = Spider.projectName + '/queue.txt'
		Spider.crawledFile = Spider.projectName + '/crawled.txt'
		self.boot()
		self.crawlPage('First Spider', Spider.baseURL)

	@staticmethod 
	def boot():
		createProjectDir(Spider.projectName)
		createDataFiles(Spider.projectName, Spider.baseURL)
		Spider.queue = fileToSet(Spider.queueFile)
		Spider.crawled = fileToSet(Spider.crawledFile)

	@staticmethod
	def crawlPage(theadName, pageURL):
		if pageURL not in Spider.crawledSet:
			print(theadName + ' is now crawling: ' + pageURL)
			print('Queue length: ' + str(len(Spider.queueSet)) + ' | Crawled: ' + str(len(Spider.crawledSet)))
			Spider.addLinksToQueue(Spider.gatherLinks(pageURL))
			Spider.queue.remove(pageURL)
			Spider.crawledSet.add(pageURL)
			Spider.updateFiles()
