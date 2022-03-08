from flask import Flask, request, jsonify, abort, render_template
from firebase_helper import read_reminder_json, create_reminder_json, delete_reminder_json
import uuid
from reply_helper import respond
import os
from datetime import date
from twilio.rest import Client
import time
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

twilio_client = Client(account_sid, auth_token)

def find_reminders_due():
    global reminders
    reminders = read_reminder_json()
    keys = list(reminders)
    keys_due = [
        i for i in keys
        if reminders[i]["due_date"] == str(date.today())
    ]
    if len(keys_due) > 0:
        send_sms_reminder(keys_due)

def send_sms_reminder(keys):
    for key in keys:
        twilio_from = os.environ["TWILIO_SMS_FROM"]
        to_phone_number = reminders[key]['phone_number']
        twilio_client.messages.create(
            body=reminders[key]['message'],
            from_=f"{twilio_from}",
            to=f"{to_phone_number}")
        delete_reminder_json(key)
        time.sleep(30)

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/daily', methods=['GET'])
def cron_job():
    find_reminders_due()
    return "Success", 200

@app.route('/uptime', methods=['GET'])
def uptime():
    return "Success", 200

@app.route('/api', methods=['GET'])
def get_reminders():
    reminders = read_reminder_json()
    return jsonify({'reminders': reminders})


@app.route('/api', methods=['POST'])
def create_reminder():
    req_data = request.get_json()

    if not all(item in req_data
               for item in ("phone_number", "message", "due_date")):
        abort(400)

    reminder = {
        'phone_number': req_data['phone_number'],
        'message': req_data['message'],
        'due_date': req_data['due_date']
    }
    reminder_id = uuid.uuid4().hex
    create_reminder_json(reminder, reminder_id)
    return jsonify({'reminder': reminder}), 201

@app.route('/api/<reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    val = delete_reminder_json(reminder_id)
    if val==False:
        abort(404)
    else:
        return jsonify({'message': 'Reminder has been removed successfully'})

@app.route("/api/message", methods=['GET'])
def post_sms():
    body = request.values.get('Body', None)
    return respond(body)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0")