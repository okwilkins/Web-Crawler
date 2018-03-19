import os

#Each website you crawl is a seperate project (folder)
def createProjectDir(directory):
	#if not used to not overwrite already exisiting project with same name
	if not os.path.exists(directory):
		print('Creating project: ' + directory)
		os.makedirs(directory)

createProjectDir('Test')