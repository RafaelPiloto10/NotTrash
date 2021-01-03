# !Trash

## Inspiration & What it does
!Trash (nɒt træʃ) aims to collect data on the amount of recyclable and compostable materials headed to landfills and prevents recyclables from going into the trash by equipping household trash cans with a camera on the underside of the lid to detect and categorize materials being discarded. 
## How we built it
For our project, we decided to create an image classifier using a Convolutional Neural Network. We trained the Neural Network on images classified as organic or recyclable using Google Cloud Platform. 
By using the weights determined through training we were able to utilize the model’s confidence interval to determine whether an object is trash, recyclable or organic. 
Our team used OpenCV to create a live feed to our model, which allows the user to present any item and get an instant classification.
Finally we incorporated the hardware portion of our project by using an Arduino to present the user with a flashing light (either red, green, or blue) to denote the classification of the object. 
For the backend we coded it to use Google API to retrieve the incoming data from the google sheets database to update the frequency of each classification within a google sheets. This is so the information can stay up to date for the consumer.
We created and designed the website and embedded a fast-updating pie chart graphical representation that models data processed by the backend to display on the Global Analytics page. 
The Global Analytics page works by displaying an image of a graph created using Google Sheets and is updated with data changed in the Sheet by the backend. 
## Challenges we ran into
Initially, the Global Analytics page embed from default Google Sheets would take 3-5 minutes to update, but we were able to improve this to update upon one page refresh. 
## Accomplishments that we're proud of and what we learned
We are proud of selecting a medium challenging project that is both prototype completable in the Hackathon period and more advanced than just one method. We learned how to structure our time much better than we have in previous hackathons. 
## What's next for !Trash
!Trash is currently patent pending and we hope that with more time and better resources we can continue to work on it by building prototypes that will more accurately reflect the data we want to display. We believe our product will encourage people to make a positive impact on our environment. 

## Built With
Python, Weebly, Google Cloud, OpenCV, Arduino
## Try it out
https://newyearnottrash.weebly.com/
