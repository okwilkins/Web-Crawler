import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'YouTube' # In Python, to denote a const. var, type it in all caps
HOMEPAGE = 'https://www.youtube.com/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = 'projects/' + PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = 'projects/' + PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # Depends on the operating system
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
