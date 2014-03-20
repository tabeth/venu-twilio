from flask import Flask, request, redirect, session
import twilio.twiml

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Add our own number to this list!
callers = {
	"+14693283305": "Tabeth",
	"+17814925607": "Rosy",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls..."""

	counter = session.get('counter', 0)

	counter += 1

	# Save the new counter value in the session
	session['counter'] = counter

	from_number = request.values.get('From')
	if from_number in callers:
		name = callers[from_number]

	else:
		name = "Monkey"


	message =  "".join([name, " has messaged ", request.values.get('To'), " ",
		str(counter), " times."])
	resp = twilio.twiml.Response()
	resp.sms(messsage)

	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)