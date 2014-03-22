from flask import Flask, request, redirect, session
import twilio.twiml
import valentine
from random import randint

SECRET_KEY = 'pineapple'
app = Flask(__name__)
app.config.from_object(__name__)

#Foods
breakfast = ''
lunch = ''
dinner = ''

#Greeting List
greeting = {
	'Ahoy.',
	'Good day.',
	'Greetings for the day.',
	'Hello.',
	'Hello there.',
	'Hey.',
	'Hi.',
	'Hi there.',
	'How are you? I hope you are having a good day!',
	'How are you doing? Hope everything is good!',
	"What's up doc?",
	"Wazzzup.",
	"What's popping?",
	"Welcome.",
	"Yo!",
	"Sup!",
}

todayGreeting = greeting[randint(0, len(greeting))]

for count in range(10):
	breakfast += + " " + valentine.menu('Breakfast', count)
	lunch += " " + valentine.menu('Lunch', count)
	dinner += " " + valentine.menu('Dinner', count)


# Add our own number to this list!


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls..."""


	counter = session.get('counter', 0)
	counter += 1
	session['counter'] = counter

	#First message
	from_number = request.values.get('From')
	message = todayGreeting + " Do you want to know today's menu? Let me know! You can say: breakfast, lunch or dinner. By the way, you can also just say breakfast, lunch or dinner and I'll immediately text you the specified menu!"
		

	#Second message
	message_body = request.values.get('Body')
	if message_body.lower() == 'breakfast':
		message = "Here's the breakfast menu: " + breakfast

	elif message_body.lower() == 'lunch':
		message = "Here's the lunch menu: " + lunch

	elif message_body.lower() == 'dinner':
		message = "Here's the dinner menu: " + dinner

	resp = twilio.twiml.Response()
	resp.message(message)


	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)