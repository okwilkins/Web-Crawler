import os

# Each website you crawl is a seperate project (folder)
def createProjectDir(directory):
	#if not used to not overwrite already exisiting project with same name
	if not os.path.exists('projects/' + directory):
		print('Creating project: ' + directory)
		os.makedirs('projects/' + directory)

# Create queue and crawled files (if not created)
def createDataFiles(projectName, baseURL):
	queue = 'projects/' + projectName + '/queue.txt'
	crawled = 'projects/' + projectName + '/crawled.txt'

	if not os.path.isfile(queue):
		# Creates a file that adds the base website to start the crawling process
		writeFile(queue, baseURL)

	if not os.path.isfile(crawled):
		# Creates empty file for the crawled urls
		writeFile(crawled, '')

###
# HOUSE KEEPING FUNCTIONS
###

# Creates a new file
def writeFile(path, data):
	file = open(path, 'w')
	file.write(data)
	file.close()

# Add data into an existing file
def appendFile(path, data):
	# with statement more compact for opening and closing files
	with open(path, 'a') as file:
		file.write(data + '\n') # \n makes the text file easier to read for humans

# Delete the conents of the file
def deleteFileContents(path):
	with open(path, 'w'):
		pass # DO NOTHING

###

# Read a file and convert each line to set items (sets don't allow the same elements to be appened)
def fileToSet(fileName):
	results = set()
	with open(fileName, 'rt') as file: # rt: read text file
		for line in file:
			results.add(line.replace('\n', '')) # Replaces the readable \n to nothing, so the computer can read
	return results

# Iterate through a set, each item will be a new line in the file
def setToFile(links, file):
	deleteFileContents(file)
	for link in sorted(link): # Sorts links into alphabetical order, for readability
		appendFile(file, link)