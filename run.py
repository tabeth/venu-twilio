from flask import Flask, request, redirect, session
import twilio.twiml
import valentine

SECRET_KEY = 'pineapple'
app = Flask(__name__)
app.config.from_object(__name__)

#Foods

breakfast = valentine.createMenu('Breakfast')
lunch = valentine.createMenu('Lunch')
dinner = valentine.createMenu('Dinner')

food = {
	"breakfast": valentine.createMenu('Breakfast'),
	"lunch": valentine.createMenu('Lunch'),
	"dinner": valentine.createMenu('Dinner'),
}

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
	session['counter'] = counter

	#First message
	from_number = request.values.get('From')
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message! Do you want to know today's menu? Let me know! You can say: breakfast, lunch, dinner, or all for all of them"
		message = message
	else:
		message = "Thanks for the message! Do you want to know today's menu? Let me know! You can say: breakfast, lunch, dinner, or all for all of them"
		message = message 
		

	#Second message
	message_body = request.values.get('Body')
	if message_body == 'breakfast':
		message = "Here's the breakfast menu: " + breakfast

	elif message_body == 'lunch':
		message = "Here's the lunch menu: " + lunch

	elif message_body == 'dinner':
		message = "Here's the dinner menu: " + dinner

	resp = twilio.twiml.Response()
	resp.message(message)


	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)