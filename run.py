from flask import Flask, request, redirect, session
import twilio.twiml
import valentine

SECRET_KEY = 'pineapple'
app = Flask(__name__)
app.config.from_object(__name__)

#Foods
breakfast = ''
lunch = ''
dinner = ''

for count in range(10):
	breakfast += valentine.menu('Breakfast', count)
	lunch += valentine.menu('Lunch', count)
	dinner += valentine.menu('Dinner', count)


# Add our own number to this list!


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls..."""


	counter = session.get('counter', 0)
	counter += 1
	session['counter'] = counter

	#First message
	from_number = request.values.get('From')
	message = "Thanks for the message! Do you want to know today's menu? Let me know! You can say: breakfast, lunchor dinner. By the way, you can also just say breakfast, lunch or dinner and I'll immediately text you the specified menu!"
		

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