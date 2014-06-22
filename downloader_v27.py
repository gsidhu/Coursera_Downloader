## Coursera_Downloader
## MIT License, 2014 Gurjot S. Sidhu

## Runs on Python 2.7 using the urllib module

import time
import urllib as urr
import os
from shutil import copyfileobj

# Enter the link to the directory where you want the downloaded files to be saved
download_directory = "/home/user/Lectures"

# Enter the download url		
link = "https://class.coursera.org/algo-004/lecture/download.mp4?lecture_id="

# Enter the increment for the ticker according to the pattern
ticker = 2

# Set a buffer time based on file size and download speed
buffer_time = 400

# OPTIONAL : If you don't want the downloaded files to have their original lecture names, you can name them as Lecture 1,2,3 ... (Although I have no idea why anyone would want to do that)
retain_original_names = True

## Kick back and relax

os.chdir(download_directory)

def download():
	count = 0
	# Set the limits of the range according to the "id" keys 	
    for i in range(1, 2000):
		count += 1

		try:		
			if retain_original_names:
			    urr.urlretrieve(link + str(i))
			else:
				urr.urlretrieve(link + str(i), "Lecture " + str(count))
		except AttributeError:
		    with urr.urlopen(link + str(i)) as in_data, open("Lecture " + str(count), 'wb') as out_video:
			    copyfileobj(in_data, out_video)
			
	    i += ticker
        time.sleep(buffer_time)
	
	print (str(count) + " videos have been downloaded.")

# Removing any temporary files left behind
urr.urlcleanup()

##############################################################################################################
## Known Issues
## If the downloaded files are named "Lecture 1,2,3 ..." even though retain_original_names is set to True - 
##		1. Python Org as finally deprecated the urlretrieve attribute
##		2. I still haven't figured out how to scrape Coursera's website
##############################################################################################################
