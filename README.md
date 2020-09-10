# ClassReport
A script to send a daily report of assignments with their respective due dates from Google Classroom.

## Install
```python
pip install -r requirements.txt
```

## Setup
First, get your clientID and secretID from Google Cloud. Sign in with the Gmail account that is associated with Google Classroom and click on the "Enable the Classroom API" button at this [link](https://developers.google.com/classroom/quickstart/python). Enter the new project name as "ClassReport", select "Desktop App" from the dropdown menu, and download the Client Configuration. This will be in the form of a json, called `credentials.json`. Move this file to the directory where you have cloned this project. This file will be necessary in authenticating the Google Classroom API. 

Then, create a file in this directory called `config.yaml`. This will store all of the email client related properties. Here's an example:
```yaml
# yaml config file for email client setup
sender: report@example.com
sender_password: reportPassword
receiver: report.receiver@example.com
```

## Run
To run the script, make sure to pass in the `config.yaml` file as well as the `credentials.json` file. 
```shell
$ python class_report.py credentials.json config.yaml
```
I am currently implementing this via a cronjob so that the email gets sent out every day at a given time. Enjoy!

