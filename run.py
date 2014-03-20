from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Add our own number to this list!
callers = {
	"+14693283305": "Tabeth",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls..."""

	from_number = request.values.get('From', None)
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message!"
	else:
		message = "Monkey, thanks for the message!"

	resp = twilio.twiml.Response()
	with resp.message("Hello, Mobile Monkey") as m:
		m.media("https://demo.twilio.com/own.png")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)