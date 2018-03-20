# Python Web Crawler
## Created by Oliver Wilkins
### 19/03/2018

This program will crawl through entire domains, exporting every link it can find into a txt file.

## Installating/Running the Project

You will not need to download any libraries, plug-in and play by: 
* Downloading or cloning the repository
* Running the main.py file
* Links which the program saves are found in the *queued.txt* and *crawled.txt* files in the [projects folder](https://github.com/HomelessSandwich/Web-Crawler/tree/master/projects) - the folder has example projects with *queued.txt* and *crawled.txt* 

## Important

* This program works by reading a webpage and extracting the links to the *queued.txt* file, when gotten round to the program will read further links from the *queued.txt* file and will then dump the then completed (crawled) webpage to the *crawled.txt* file
* You can try to trawl through massive domains, with many links - this will take a *VERY* long time however. 
* Also note that you may need to change the NUMBER_OF_THREADS variable in the [spider.py](https://github.com/HomelessSandwich/Web-Crawler/blob/master/main.py) (line 12) file. This will depend on your operating system.
```python
NUMBER_OF_THREADS = 8
```

## Updates for the Future
* Add a tree view for all the links found
* Reduce the number of decoding errors
* Fix some URLs completely shutting down threads and ultimately the whole program. This issue is described in detail [here](https://github.com/HomelessSandwich/Web-Crawler/issues/1).
