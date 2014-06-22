#Coursera_Downloader
===================

A handy tool to automatically download videos from Coursera or iTunes U. (No, it does not download *all* of Coursera)


##Pre-requisites:

1. You must be able to access the lecture videos at the time of execution of code.
  1. The course videos must be available for download.
  2. You must be signed in to your Coursera account in your default browser.
2. You should have the download link for the lecture videos.

##HOW-TO run this code:

1. First off, you MUST (*yet*) specify the downloads directory. If you don't specify any, the code will fail. (*yet*). On Windows it'll look something like - `C:\My_Folder\...`, and on Ubuntu like this - `/home/User_Name/My_Folder/`.

2. Go to the Lecture Video page of the course on Coursera. Check the Download link for each lecture, it should look something like this: 
	`"https://class.coursera.org/<Course Name>/lecture/download.mp4?lecture_id=<X>"`.
The last part - `id=<X>`, is the one we are looking for; the value of X will differ for each lecture video and will form a pattern. Usual patterns are odd numbers, even numbers or some other simple arithmetic progression.

2. Once you have the pattern, open the .py file in an editor. In the code, enter the download url as a string to the `link` variable. Make sure you type only till the `"..._id="` part and not enter any particular value for lecture_id. 

3. Next, add a value to the `ticker` variable based on whatever pattern the ids follow. In case it is an alternating series, just specifying `1` should work for you.

4. Finally, based on your internet connection provide a `buffer_time` between consecutive downloads. This is done to ensure your files download one by one and not all at the same time.

5. Save the code and run it! If you need help running the code, [check this out](https://www.google.co.in/search?client=ubuntu&channel=fs&q=how+to+run+py+files&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=0EinU6uoDeHA8ge2wICAAQ)

Note - The values I have input in my code are for an Introduction to Algorithms course which had an alternating pattern between lecture_ids. The 400 second buffer time is based on my internet connection's download speed.
