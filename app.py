from flask import (Flask, render_template, request)

import random
import json

app = Flask(__name__,template_folder="templates")

APPLICATION_NAME = "blackjacknow"

@app.route('/')
def homepage():
	return render_template('index.html')


@app.route('/scenario')
def scenario():
	hard = request.args.get('hh')
	soft = request.args.get('sh')
	pairs = request.args.get('ph')

	dlr = ['2','3','4','5','6','7','8','9','10','A']

	currRuleSet = {}

	with open('static/rules.txt','r') as f:
		allRules= json.load(f)

	if (pairs=='true'):
		currRuleSet.update(**allRules['pairs'])

	if (soft=='true'):
		currRuleSet.update(**allRules['soft'])

	if (hard=='true'):
		currRuleSet.update(**allRules['hard'])

	if (currRuleSet == {}):
		currRuleSet = {**allRules['hard'], **allRules['soft'],**allRules['pairs']}



	playerHand = list(currRuleSet.keys())

	pChoice = random.choice(playerHand)
	dChoice = random.choice(dlr)
	decision = currRuleSet[pChoice][dChoice]

	context = {'playerCard':pChoice,
			   'dealerCard':dChoice,
			   'decision':decision}

	print(hard,soft,pairs)


	return render_template('scenario.html',**context)
