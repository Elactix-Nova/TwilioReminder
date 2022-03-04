# Reminder App
### _Pls gloss over the fact that this program is obsolete due to smartphones, therefore if u own one, I have to ask u to click away pls...only my flip phone bros allowed here :)_

[![](https://camo.githubusercontent.com/9926be6d28a0275bd81445560f4ea39b245506a9e038244db2e74a0d28a969d0/68747470733a2f2f64336b326630733376717173396f2e636c6f756466726f6e742e6e65742f6d656469612f66696e616c2f36616565303662322d323161382d343631332d396337302d3934343164636131336432632f776562696d6167652d43384442393238302d334244442d343332442d414434373245393246374345334431312e706e67) ](https://www.twilio.com/)

Reminder App is a cool little piece of code, that helps people to keep track of events. The best thing about this program is that all reminders and delivered via messages so even people with older phones can use this program.

## Features

- > Add reminders via message.
- > At beginning of each day, all the due reminders are sent via message to receivers.
- > Each reminder is assigned a UID, which can be used to delete reminders via API request
- > Addition of reminders also supported via API request.
- > 24 x 7 monitoring of web-server via Cron-Job)

## How to Setup The App

To get the app running properly, you need to host a web-server via any platform of your choice. For the purpose of this project, I have chosen Heroku.
> [Heroku] - Cloud Application Platform

Before starting, fork this repository to your github account as it will be needed for connection via Heroku.
Once you have created an Heroku account, create a new app and connect your github account, then choose the corresponding repository and enable automatic deploys, then click on deploy branch to deploy your web-server.
## Troubleshooting

If the web-server does not run successfully, then you can check the logs for your app via "https://dashboard.heroku.com/apps/'your-app-name-here'/logs"

The most common troubleshooting step is to check whether the dyno formation window in the overview tab, shows the command to be run at startup of web-server.

If the window is blank, then create a document called "Procfile" with the following content and save it to the root directory

`web gunicorn --bind 0.0.0.0:$PORT main:app`
 
## Dependencies

| Library | Version |
| ------ | ------ |
| Gunicorn | 20.1.0 |
| Twilio | 7.7.0 |
| Flask | 2.0.3 |
| Python-Dateutil | 2.8.2 |
| Python-Dotenv | 0.19.2|

## Features to be added soon

>One new feature that will be added soon, is that of group reminders which can be added by a group member and sent to everyone in the group on the due date.

   [Heroku]: <https://www.heroku.com/>
