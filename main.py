from flask import Flask, request, jsonify, abort
from reminder_json_helper import read_reminder_json, create_reminder_json, delete_reminder_json
import uuid
from sms import option1

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def uptime():
    return 200

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


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


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
    return option1(body)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0")