import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'GitHub' # In Python, to denote a const. var, type it in all caps
HOMEPAGE = 'https://github.com/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = 'projects/' + PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = 'projects/' + PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # Depends on the operating system
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exists)
def createWorkers():
	for _ in range(NUMBER_OF_THREADS): # use _ as you're not using it in formulas etc., it is convention
		t = threading.Thread(target = work)
		t.daemon = True # Dies whenever the main process exists
		t.start()

# Do the next job in the queue
def work():
	while True:
		url = queue.get()
		Spider.crawlPage(threading.current_thread().name, url)
		queue.task_done()

# Each queued link is a new job
def createJobs():
	for link in fileToSet(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

# Check if there are items in the queue, if so, crawl them
def crawl():
	queueLinks = fileToSet(QUEUE_FILE)
	if len(queueLinks) > 0:
		print(str(len(queueLinks)) + ' links in the queue')
		createJobs()

createWorkers()
crawl()