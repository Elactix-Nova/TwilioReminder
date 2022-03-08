import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()

config = {
  "apiKey": os.environ.get("apiKey"),
  "authDomain": os.environ.get("authDomain"),
  "databaseURL": os.environ.get("databaseURL"),
  "storageBucket": os.environ.get("storageBucket"),
  "serviceAccount": "cert.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def read_reminder_json():
    data = db.child("reminders").get()
    return data.val()

def create_reminder_json(reminder, reminder_id):
    data = db.child("reminders").get()
    db.child("reminders").child(str(reminder_id)).set(reminder)

def delete_reminder_json(reminder_id):
    data = db.child("reminders").get().val()
    keys = list(data)
    for i in keys:
        if i==reminder_id:
            db.child("reminders").child(i).remove()
            return True
            break
    else:
        return False