from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Add our own number to this list!
callers = {
	"+14693283305": "Tabeth",
	"+17814925607": "Rosy",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls..."""

	from_number = request.values.get('From', None)
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message!"
	else:
		message = "Thanks for the message!"

	resp = twilio.twiml.Response()
	resp.message(message)

	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)