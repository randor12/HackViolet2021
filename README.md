# Hack Violet 2021
This is our Hack Violet Project for 2021. We developed a website using Flask. The purpose 
of our application was in order to create a more welcoming enviroment for people to post under.
Our group developed a Machine Learning model to perform sentiment analysis on text that is posted on our
site. 
By using Artificial Intelligence, we are able to ensure that only texts that are considered "positive" 
by the AI are allowed to be posted. We developed our machine learning model using the NLTK for natural language 
processing. This ultimately lead to a model we found to be about 75% accurate from our test data. 
We then decided to implement this in on "social media" as a way to see how the world would change 
if people were only allowed to post "Positive" comments on our page. 
The prompt we would like to inspire on people is "What good thing happened in your day today?" 
Ideally, this could serve as a way for people to improve their own self, while taking the time to
reflect on themselves to perform self-care on themselves. 
The application is held on Google Cloud similar to an EC2 instance on AWS and is registered on
Domain.com.
With this project, we hope you enjoy our project: "Daily Joy", a social media app that 
only looks for the positives.

# AUTHORS:
- Ryan Nicholas, Computer Science - Junior
- Matthew Gonley, Computer Science - Junior
- Justin Cheng, Computer Science - Junior
- Roi Pascual, Computer Science - Junior

# REQUIREMENTS

- Must have Python 3 installed on computer and pip or anaconda
- Must have MySQL

# HOW TO RUN LOCALLY

1. Download the code using:
- `$ git clone https://github.com/randor12/HackViolet2021.git`
2. Enter into the folder
- `$ cd HackViolet20201`
3. Downloaded Required Packages
- `$ pip install -r requirements.txt`
4. Run test
- `$ pytest`
5. Set up .env file
- `$ touch .env`
- `$ nano .env`
6. Add the following into the file 
`
USER_DATABASE='mysql-username-here'
PASS_DATABASE='mysql-password-here'
SECRET_KEY='S3CRETalsjdfklj'
`
7. Set up the tables with the script in createTable.sql

8. Run the application
- `$ python app.py`
9. Go to your web browser and type in the URL: `http://localhost:5000`

# Server Side
The GET, POST, PUT Requests are handled in the `app.py` file.
This uses Flask to control the routing information each request and
handles the back end development behind the website as a controller

# WEB

- The HTML files are placed inside the `templates` folder
- The CSS and JavaScript files are placed inside the `static` folder
- Extra Python Files to Help with the back end are placed in the `models` folder
