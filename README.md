Coursera_Downloader
===================

A handy tool to automatically download videos from Coursera or iTunes U. (No, it does not download *all* of Coursera)


##Pre-requisites:

1. You must be able to access the lecture videos at the time of execution of code.
  1. The course videos must be available for download.
  2. You must be signed in to your Coursera account in your default browser.
2. You should have the download link for the lecture videos.

##HOW-TO run this code:

1. Go to the Lecture Video page of the course on Coursera. Check the Download link for each lecture, it should look something like this: 
	`"https://class.coursera.org/<Course Name>/lecture/download.mp4?lecture_id=<X>"`.
The last part - `id=<X>`, is the one we are looking for; the value of X will differ for each lecture video and will form a pattern. Usual patterns are odd numbers, even numbers or some other simple arithmetic progression.

2. Once you have the pattern, open the .py file in an editor (I use IDLE). In the code, enter the download link as a string in the parenthesis after the `web.open` function. Make sure you type only till the "..._id=" part and not enter any particular value for lecture_id. 

3. In the next line, assign an algorithm to the iterable "i" based on whatever pattern the ids follow. In case it is an alternating series, `i += 1` should work for you.

4. Finally, based on your internet connection provide a **buffer time** between consecutive downloads. In the parenthesis after the `time.sleep` function enter a rough value (in seconds) of the time it takes for one video to download.

5. Choose which folder you wish to download your lectures to and enter the link to that folder in the `os.chdir` function.

Save the code and run it!

Note - The values I have input in my code are for an Introduction to Algorithms course which had an alternating pattern between lecture_ids. The 400 second buffer time is based on my internet connection's download speed.
