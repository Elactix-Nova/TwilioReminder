import datetime
from twilio.twiml.messaging_response import MessagingResponse
import uuid
from firebase_helper import create_reminder_json

def check_date(date):
    year, month, day = [int(i) for i in date.split('-')]
    correctDate = None
    try:
        datetime.datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate

def check_number(phone_number):
    correctNumber = None
    try:
        int(phone_number)
        correctNumber = True
    except ValueError:
        correctNumber = False
    return correctNumber

def respond(body):
    resp = MessagingResponse()
    
    body=body.split('\n')
    if len(body)!=3:
        resp.message('Incorrect Format\n1st Line should be receiver\'s phone number (with country code)\n2nd Line should be reminder message\n3rd Line should be date in "YYYY-MM-DD" format\n\nFor Example\n+919810273548\nReminder Message\n2021-09-30')
    else:
        if not check_date(body[2]):
            resp.message('Incorrect Date\nPlease type in "YYYY-MM-DD" format')
        elif not check_number(body[0]):
            resp.message('Incorrect Phone Number\nPlease type as\n[+] [country code] [phone number including area code]')
        else:
            resp.message('Reminder successfully added', action="/MessageStatus")
            reminder = {
                'phone_number': body[0],
                'message': body[1],
                'due_date': body[2]
            }
            reminder_id = uuid.uuid4().hex
            create_reminder_json(reminder, reminder_id)

    return str(resp)