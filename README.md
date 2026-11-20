#MiniForum

MiniForum is a simple gaming themed discussion forum that I am developing for my Secure App Programming project at NCI(National College of Ireland)

The aim of my project is to create a working web application and demostrate common security vulnerabilities, how they can be exploited, and how they can be prevented through secure coding practices.

##Technologies used for the project

-Python
-Flask
-SQLite3
-HTML, CSS and JavaScript

##Features

The application will allow users to:
-Register and Log in to an account
-Create gaming discussion threads
-View and search for threads
-Comment on discussions
-View their user profile

##Security

The main focus of my project is to demostrate the difference between insecure and secure code.

The following vulnrabilities will be covered:
-SQL Injection
-Reflected XSS
-DOM based XSS
-Stored XSS
-Sensitive data exposure

There will be 2 seperate versions of the app, one that contains vulnerabilities and another with security measures implemented to prevent them.

The versions will be maintained in seperate Git Branches.

##How to Run the Application

1.Clone or donwload the repo
2.Open the project folder inn VS code.
3.Create a Python virtual env:
    'py -m venv .venv'

4.Activate the vm:
    '.\.venv\Scripts\Activate.ps1'

5.Install the required packages:
    'python -m pip install -r requirements.txt'

6.Run the app:
    'python app.py'

7.Open 'http://127.0.0.1:5000' in your browser.

##Project Progress

The Flask application has been set up and tested locally.

The forum features, database and security implementations are currently being developed.

##Note

The insecure version of MiniForum is made for educational prposes and should only be tested in a local enviroment.

