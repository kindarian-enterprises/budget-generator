def generate_budget(user_data):
	"""Takes the user data and does some calculations to reach desired goals set"""
	goal = user_data['savingsGoal']
	curr_saving = user_data['currentSaving']
	pay = user_data['income']
	
	response = 0
	if curr_saving >= goal:
		response = 0
	else:
		while curr_saving < goal:
			response += 1
			curr_saving = curr_saving + pay
	return response