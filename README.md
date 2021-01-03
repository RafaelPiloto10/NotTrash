# !Trash

## Inspiration & What it does

!Trash (nɒt træʃ) aims to prevent recyclables from going into the trash by equipping household trash cans with a camera on the underside of the lid to detect and categorize materials being discarded. Our inspiration stems from the infamous New Years Resolution: "I am going to be environmentally cleaner this year!". !Trash, helps you stay clean!

## How we built it

For our project, we decided to create an image classifier using a Convolutional Neural Network. We trained the Neural Network on 22K images classified as organic or recyclable using the Google Cloud Platform and TensorFlow.

By using the weights determined through training we were able to utilize the model’s confidence interval to determine whether an object is trash, recyclable or organic. 

Our team then used OpenCV to create a live video stream to our model, which allows the user to present any item to the camera and get an instant classification of the waste.

Finally, we incorporated a hardware portion to our project using an Arduino to present the user with a flashing light (either red, green, or blue) to denote the classification of the object. This acts as visual feedback for the user for when !Trash is embedded into small devices attached to trash can lids.

We coded our backend to use the Google Cloud Services and API to retrieve the incoming analytics from our classification to update the frequency of each classification within a google sheet. This is so the information can stay up to date for the consumer and displayed graphically on our [website](https://newyearnottrash.weebly.com/).

The front-end was created and designed to embed a fast-updating pie chart graphical representation that models data processed by the backend to display on the Global Analytics page.

The Global Analytics page works by displaying an image of a graph created using Google Sheets and is updated with data changed in the Sheet by the backend automatically. 

## Challenges we ran into

Initially, the Global Analytics page embedded from default Google Sheets would take 3-5 minutes to update, but we were able to improve this to update upon one page refresh.

Another issue our team faced was compatibaility issues. Since 3 out of 4 members of our team had laptops running Apple's M1 chip, we faced issues where software was incompatiable with our devices. Most noticeable, Tensorflow and OpenCV are not easily compatiable. We were able to get around this by recompiling the source code into ARM instruction to be able to use our dependencies. We were also able to take advantage of **Google Cloud in this regard to train our model in the cloud** since SciPy is not readily compatiable with Apple Silicon (M1 Chip). 

## Accomplishments that we're proud of and what we learned

We are proud of selecting a challenging project that is both prototype completable in the Hackathon period and more advanced than just one method. We learned how to structure our time much better than we have in previous hackathons.

Most noticeably, we are proud of our ability to create a project out of something so complex. **One of our members had to learn Python from scratch!** We also had to learn TensorFlow and OpenCV as no one in our team had experience with Machine Learning. 

## What's next for !Trash
**!Trash is currently patent pending** and we hope that with more time and better resources we can continue to work on it by building prototypes that will more accurately reflect the goals we want to display. We believe our product will encourage people to make a positive impact on our environment. 

## Built With
Python, Tensorflow, OpenCV, Google Cloud, OpenCV, Arduino, Weebly

## Try it out
https://newyearnottrash.weebly.com/
