from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'NewSecret'

@app.route('/')
def index():
	# session.clear()
	# print session['gold']
	if 'gold' in session:
		pass
	else:
		print 'here'
		session['gold'] = 0	
		session['activities'] = []
	if 'activities' not in session:
		session['activities'] = []	
	reverse_list = reversed(session['activities'])
	return render_template('index.html', gold = session['gold'], activities = reverse_list)

@app.route('/process_money', methods=["POST"])
def play():		

	if request.form['building'] == 'farm':
		gold_count = random.randrange(10,20)
		session['gold'] += gold_count
		session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
	elif request.form['building'] == 'cave':
		gold_count = random.randrange(5,10)
		session['gold'] += gold_count
		session['activities'] += ["<p>You won %s</p>" % str(gold_count)] 
	elif request.form['building'] == 'house':
		gold_count = random.randrange(5,10)
		session['gold'] += gold_count	
		session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
	elif request.form['building'] == 'casino':
		luck = random.randrange(1,10)
		gold_count = random.randrange(0,50)
		if luck > 7: 
			session['gold'] += gold_count
			session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
		else:	
			session['gold'] -= gold_count	
			session['activities'] += ["<p>You lost %s</p>" % str(gold_count)] 
	return redirect('/')		

@app.route('/reset')	
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)



# to redirect: return redirect('/route_goes_here')