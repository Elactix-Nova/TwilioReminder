# Reminder App

<p float="left">
   &nbsp;&nbsp;
  <img src="https://camo.githubusercontent.com/9926be6d28a0275bd81445560f4ea39b245506a9e038244db2e74a0d28a969d0/68747470733a2f2f64336b326630733376717173396f2e636c6f756466726f6e742e6e65742f6d656469612f66696e616c2f36616565303662322d323161382d343631332d396337302d3934343164636131336432632f776562696d6167652d43384442393238302d334244442d343332442d414434373245393246374345334431312e706e67" width="200"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://freepngimg.com/thumb/python_logo/1-2-python-logo-png.png" width="200"/> 
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Heroku_logo.svg/2560px-Heroku_logo.svg.png" width="200"/>
</p>

Reminder App is a cool little piece of code, that helps people to keep track of events. The best thing about this program is that all reminders and delivered via messages so even people with older phones can use this program.

## Features

-  > Add reminders via message.
-  > At beginning of each day, all the due reminders are sent via message to receivers.
-  > Each reminder is assigned a UID, which can be used to delete reminders via API request
-  > Addition of reminders also supported via API request.
-  > 24 x 7 monitoring of web-server via Cron-Job

## How to Setup The App

### 1. Setting up the project on your device

1. Clone the repository / Download and unzip it to a folder on your device.

2. `cd` into the project directory using command prompt (windows) or terminal (macOS) and run the following command to set up a python virtual environment<br/><br/>`python -m  venv venv`<br/><br/><b>Note -</b> Don't use windows terminal  as it does not allow running of scripts ( a step which will come later on)

3. Next we need to activate the virtual environment, which can be done on a Windows device using<br/><br/>`venv\Scripts\activate`<br/><br/>*Please note the use of backslash (\\) here and not frontslash (/)<br/><br/>If you're using a MacOS or Linux device, then use the following command<br/><br/>`source venv/bin/activate`<br/><br/>If you have set up and activated the virtual environment correctly, there should now be a (venv) written next to your project directory's path.

4. Next we need to install all the project dependencies, which can be done by using pip<br/><br/>`pip install -r requirements.txt`

### 2. Setting up Firebase

The app uses Google Firebase's Realtime Database to store the reminders. This is to prevent the existing reminders from getting deleted every time a new state of the branch is automatically deployed to Heroku.

For integrating Firebase with the app, we need to first set up a new project and within that project we need to create a new realtime database. While setting up the database, pls ensure that it starts in locked mode thus allowing only authenticated users to access and modify it. After that is done, we need to add the service account credentials that will allow the program to authenticate with Firebase as an admin and add/delete reminders.

1. Sign into your account and open your created project. Click on the settings icon and select Project Settings. Once inside project settings, scroll down to the your apps card and click on the web app icon (the one that looks like '</>'). Once you've named the app, you can view the credentials that will be required under the Add Firebase SDK. Out of all the given credentials, we need only the following for storing later on.

| Key | Value |
| ------ | ------ |
| apiKey | apiKey |
| authDomain | projectId.firebaseapp.com |
| databaseURL | https://databaseName.firebaseio.com |
| storageBucket | projectId.appspot.com |

2. The next thing we require is our private key certificate. For getting that you need to nagivate to the project settings window again, and click on service accounts. Once you have opened that,  you would be able to see the service account which is going to be used to authenticate the program's access to your database. On the same page, scroll down and click on generate new private key. Once you have downloaded the file, rename it to 'cert.json' and move it to the project directory which you had created earlier.

### 3. Setting up Twilio

On your [Twilio Console](https://twilio.com/console), copy your Account SID and Auth Token. We are going to need these values to authenticate with the Twilio service. You will also need to set up a Twilio phone number that can send SMS messages. You can add a phone number to your account in the [Buy a Number](https://www.twilio.com/console/phone-numbers/search) page if you don’t already have one.

### 4. Setting up Heroku

To get the app running properly, you need to host a web-server via any platform of your choice. For the purpose of this project, I have chosen Heroku.

> [Heroku] - Cloud Application Platform

Before you can deploy to Heroku, we need to upload all our files to Github. First navigate to your project directory and create a .gitignore file with the following contents.

```
venv
__pycache__
```

If you're storing your environment variables on your local machine for testing on a .env file, then you can go ahead and add that to .gitignore as well.

Then create a private repository on Github and commit all the contents of the project directory on your local machine to the repository. The gitignore file is present so that we can ignore any folders/files in your repository that don't need to be committed to the repository.

1. After uploading your project to Github, you need to create a Heroku account to deploy the app.

2. Once you have created a Heroku account, create a new app. Once created, navigate to the settings tab in the project dashboard and scroll down to Config Vars.

3. We are using Config Vars to store all our authentication variables secure and allow us to use them without the creation of a .env file.</br></br>In the Config Vars tab, add the following keys and values (obtained from steps 2 and 3)

| Key | Value |
| ------ | ------ |
|TWILIO_ACCOUNT_SID | XXXXXXXXXXX
|TWILIO_AUTH_TOKEN | XXXXXXXXXXX
|TWILIO_SMS_FROM | XXXXXXXXXXX
| apiKey | apiKey |
| authDomain | projectId.firebaseapp.com |
| databaseURL | https://databaseName.firebaseio.com |
| storageBucket | projectId.appspot.com |

<b>Note</b> - For the Twilio phone number use the E.164 format.

4. Once you have created an Heroku account, create a new app and connect your Github account, then choose the repository you had just created and enable automatic deploys, then click on deploy branch to deploy your web-server.

### 5. Linking to Twilio

After you have deployed your app, make sure it is running correctly by clicking on the view button. If everything works out correctly then you should be able to see the landing page.

Next step is to link the app to our Twilio number so that everytime someone sends a message to that number, the corresponding HTTP request is raised and our app can return the message required to be sent back to the sender and successfully add reminders as well.

In the Twilio console, navigate to the active numbers window under Phone Numbers > Manage > Active Numbers. Click on the number which you had purchased and scroll down to messaging. In the messaging tab, you need to add the link of your web app to the 'A MESSAGE COMES IN' text box, along with the corresponding app route.

For eg. If the link to your app is 'myapp.herokuapp.com', then you need to add '/api/message' at the end as well. So that the link you enter in the box becomes 'myapp.herokuapp.com/api/message'

### 6. Testing
 
That's it! You have finally set up the Twilio Reminder App, now you can use any of your personal phone numbers to send a text to your Twilio number and if everything works out correctly you should receive a text back and be able to set up your own reminders.

### 6. Final Step (Setting up a Cron-Job)

Once you have verified that the web server runs correctly, we can complete the final step by using a Cron-Job to initiate a request to our server at 12:00 AM of each day so that all the pending reminders for that day get automatically delivered to their respective recipients.

1. Set up a Cron-Job account and navigate to the dashboard.

2. In the cronjobs tab, click on CREATE CRONJOB

3. Give the cronjob an appropriate title and in the url field, fill the url of your Heroku app along with the "/daily" route at the end. For Eg. 'myapp.herokuapp.com/daily' and click on create.

4. Set the execution schedule to Every Day at 0:00 and in the notifications tab, turn off all the notification buttons. (The notifications are turned off because the app takes some time to send reminders which causes a timed out error on Cron-Job, resulting in an error mail everyday)

5. Similarly set up a new Cron-Job but this time with the route "/uptime", set the execution schedule to every 15 min and this time turn on all notifications so that you will get informed whenever your app stops running due to any reason.

## Troubleshooting

If the web-server does not run successfully, then you can check the logs for your app via "https://dashboard.heroku.com/apps/'your-app-name-here'/logs"

The most common troubleshooting step is to check whether the dyno formation window in the overview tab, shows the command to be run at startup of web-server.
  
If the window is blank, then check whether your repository has a "Procfile" with the following content and save it to the root directory

`web gunicorn --bind 0.0.0.0:$PORT main:app`  

If not then you can create it, commit to your repository and deploy to Heroku once again, which should then work correctly.

## Dependencies

| Library | Version |
| ------ | ------ |
| Gunicorn | 20.1.0 |
| Twilio | 7.7.0 |
| Flask | 2.0.3 |
| Python-Dateutil | 2.8.2 |
| Python-Dotenv | 0.19.2|
| Pyrebase4 | 4.5.0 | 

## Features to be added soon

>One new feature that will be added soon, is that of group reminders which can be added by a group member and sent to everyone in the group on the due date.

[Heroku]: <https://www.heroku.com/>
