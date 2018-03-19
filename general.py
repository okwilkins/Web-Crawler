import os

# Each website you crawl is a seperate project (folder)
def createProjectDir(directory):
	#if not used to not overwrite already exisiting project with same name
	if not os.path.exists(directory):
		print('Creating project: ' + directory)
		os.makedirs(directory)

# Create queue and crawled files (if not created)
def createDataFiles(projectName, baseURL):
	queue = projectName + '/queue.txt'
	crawled = projectName + '/crawled.txt'

	if not os.path.isfile(queue):
		# Creates a file that adds the base website to start the crawling process
		writeFile(queue, baseURL)

	if not os.path.isfile(crawled):
		# Creates empty file for the crawled urls
		writeFile(crawled, '')

# Creates a new file
def writeFile(path, data):
	file = open(path, 'w')
	file.write(data)
	file.close()