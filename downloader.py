## Coursera Download Lecture Videos
## Copyright (c) 2013 Gurjot S. Sidhu

import time
import webbrowser as web
import os

def download():
	# Enter the link to the directory where you want the downloaded files to be saved
	os.chdir("download_directory")

	# Set the limits of the range according to the "id" keys 	
    for i in range(1, 170):
		# Enter the download url		
        web.open('https://class.coursera.org/algo-004/lecture/download.mp4?lecture_id=' + str(i))

		# Increment the ticker according to the pattern
        i += 1

		# Set a buffer time based on file size and download speed
        time.sleep(400)
