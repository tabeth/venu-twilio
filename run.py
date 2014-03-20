from flask import Flask, request, redirect
import twilio.twiml
import valentine

app = Flask(__name__)

#Foods
breakfast = valentine.createMenu("Breakfast")
lunch = valentine.createMenu("Lunch")
dinner = valentine.createMenu("Dinner")

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
		message = callers[from_number] + ", thanks for the message! As you've requested, here's today's breakfast menu"
	else:
		message = "Thanks for the message! As you've requested, here's today's breakfast menu"

	resp = twilio.twiml.Response()
	resp.message(message)
	resp.message(breakfast)

	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)