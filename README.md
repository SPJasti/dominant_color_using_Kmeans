# dominant_color_using_Kmeans
this code will check each pixel and apply K Means clustering to find out a dominant colour . 

https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/notH_4.jpg
sample image for testing 

![sample image](https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/notH_4.jpg)

sample image's plot 
https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/plot1.png
![sample images's - plot ](https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/plot1.png)

sample image's - dominance in descending order
https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/Dominant1.png
![sample image's - dominance in descending order](https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/Dominant1.png)

the original sample image i took had over 22500 pixel hence it took made a lot more iterations .
i resized the image using *open CV* to 100x100 pixels now its 125% faster , sure there is datalot but in such case it can't be helped 

i used this code for my project of handwash management system ( * soon whole project will be uploaded with a video on youtube *)
even there i used resize because where i had to showcase the project internet connectivity was not available hence no *google firebase *
just a raspberry pi doing all the computing . i have added flags so that if someone is willing to use the code you will understand what 
problem is that you are facing .

# hex_color.py
for notH_1.jpg
![sample image for this code](https://github.com/SPJasti/dominant_color_using_Kmeans/blob/master/notH_1.jpg)

hist - [0.23961661 0.275449   0.1242441  0.16172985 0.19896044]
*will change for same image upon execution of code*

cluster_centers - [[ 43.30203808  82.52354433  25.58764615]
 [169.38920051 145.72142132 118.39147208]
 [107.77231816 160.36423469 192.88628565]
 [ 40.01361515  97.08099931 133.81868084]
 [199.72480743 207.39182582 201.39465724]]
 *will change for same image upon execution of code*

Hex codes are:  ['#a99176', '#2b5219', '#c7cfc9', '#276085', '#6a9fc0']
*will no change for same image upon execution of code*


