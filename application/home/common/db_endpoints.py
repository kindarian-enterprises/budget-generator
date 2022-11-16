from mongoengine import *
from application.home.common.config import DB_ROUTE, DATE_PATTERN
import random
from datetime import datetime

connect(DB_ROUTE)

class Budget(Document):
	goal = IntField()
	timeUntilGoal = IntField()
	monthlySpending = IntField()
	monthlySaving = IntField()
	dateCreated = dateTimeField()
	budgetId = IntField(primary_key=True, unique=True)

def readSpecific(budget_id):
	return_value = []
	for budget in Budget.objects:
		if budget.budgetId == budget_id:
			return_value.append({"date": budget.dateCreated, "goal": budget.goal, "time": budget.timeUntilGoal, "spending": budget.monthlySpending, "saving": budget.monthlySaving, "id": Budget.budgetId})
	return return_value

def readAll():
	return_value = []
	for budget in Budget.objects:
		return_value.append({"date": budget.dateCreated, "goal": budget.goal, "time": budget.timeUntilGoal, "spending": budget.monthlySpending, "saving": budget.monthlySaving, "id": Budget.budgetId})

def create(queryParams):
	temp_id = random.randint(1, 50_000) + random.randint(1, 50_000) + random.randint(1, 50_000)
	temp_id = temp_id[:10]

	budget = Budget(budgetId = temp_id)
	budget.goal = queryParams.goal
	budget.timeUntilGoal = queryParams.timetogoal
	budget.monthlySpending = queryParams.spend
	budget.monthlySaving = queryParams.save
	now = datetime.now()
	budget.dateCreated = datetime.strftime(now, DATE_PATTERN)
	budget.save()
	return readSpecific(temp_id)

def delete(budget_id):
	Budget.objects(budgetId=budget_id).delete()