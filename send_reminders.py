import os
from reminder_json_helper import read_reminder_json, delete_reminder_json
from datetime import date
from twilio.rest import Client
import time
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

twilio_client = Client(account_sid, auth_token)

def find_reminders_due():
    reminders = read_reminder_json()
    reminders_due = [
        reminder for reminder in reminders
        if reminder['due_date'] == str(date.today())
    ]
    if len(reminders_due) > 0:
        send_sms_reminder(reminders_due)

def send_sms_reminder(reminders):
    for reminder in reminders:
        twilio_from = os.environ["TWILIO_SMS_FROM"]
        to_phone_number = reminder['phone_number']
        twilio_client.messages.create(
            body=reminder['message'],
            from_=f"{twilio_from}",
            to=f"{to_phone_number}")
        delete_reminder_json(reminder["id"])
        time.sleep(30)

find_reminders_due()