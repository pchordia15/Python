"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

"""

def income_tax(state,gross):
	state_tax = {'CA': 17, 'NY': 9, 'TX': 10, 'MA': 12}

	#Federal tax
	net = gross - (gross * 0.10)

	if state in state_tax:

		#state tax
		net = net - (gross *state_tax[state] / 100)
		print("Net income is: " + str(net))
	else:
		print("State is not in the list")

income_tax('CA',50000)