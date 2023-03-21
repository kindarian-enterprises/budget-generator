import pytest
from mongoengine import connect
from datetime import datetime, timezone

@pytest.fixture()
def mock_get_db_connection(mocker):
    return mocker.patch(
        'application.budget.db.get_db_connection',
        return_value=connect(
            'mongoenginetest',
            host='mongomock://localhost'
        )
    )

HOME_PAGE_TEST_DATA = '''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
  <h1 class="hMain">Welcome!</h1>
  <p class="welcomeP">
    Thank you for using out budget generator! This website allows you to
    generate and download a quick budget on the fly based on some values that
    you specify. This is currently in an early version and will have
    budget-saving capabilities and user login available in later releases
  </p>
  <a href="/form"><button class="quickButton">Make Quick Budget!</button></a>
</div>
</div>
  </body>
</html>'''

ABOUT_PAGE_TEST_DATA = '''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
  <h1 class="hMain">How it Works</h1>
  <p class="welcomeP">
    This website allows you to enter in various values about your budget (i.e... monthly bills, amount in savings, savings goals and etc.) and have a nicely organized spreadsheet of a budget plan returned to you. In the background we are taking your data and preforming mathematical calculations to determine the values to return to you  
  </p>
  <a href="/form"><button class="quickButton">Make Quick Budget!</button></a>
</div>
</div>
  </body>
</html>'''

FORM_PAGE_TEST_DATA = '''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
  <h1 class="hForm">Please Enter Your Budget Info</h1>
  <div class="form">
    <h2 class="h2Form">Enter Here</h2>
    <form action='/display' method="post" class="innerForm">
      <div class="myLabel">
      <br />
        <label class="textLabel" for="month">Monthly Income</label><br />
        <br />
        <label class="textLabel" for="monthPay">Monthly Payments</label><br />
        <br />
        <label class="textLabel" for="savings">Current Savings</label><br />
        <br />
        <label class="textLabel" for="spending">Desired Monthly Spending</label
        ><br />
        <br />
        <label class="textLabel" for="savingGoal">Savings Goal</label><br />
        <br />
      </div>
      <div class="formInpt">
      <br />
        <input class="textInpt" type="text" id="month" name="month" />
        <input class="textInpt" type="text" id="monthPay" name="monthPay" />
        <input class="textInpt" type="text" id="savings" name="savings" />
        <input class="textInpt" type="text" id="spending" name="spending" />
        <input class="textInpt" type="text" id="savingGoal" name="savingGoal" />
      </div>
      <button type="submit" class="quickButton">Create Budget!</button>
    </form>
  </div>
</div>
</div>
  </body>
</html>'''

DISPLAY_PAGE_TEST_DATA = '''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
  <div style="width: 49%; float: left">
    <h1 class="hDisplay">Your Budget Breakdown</h1>
    <ul class="displayList">
      <li>The first value is your goal.</li>
      <li>
        The second value represents the amount you need to save every month in
        order to reach your goal.
      </li>
      <li>
        The third value represents the amount you are able to spend each month
      </li>
      <li>
        The fourth value is the time it will take until in months until you
        reach your goal at this current saving rate.
      </li>
    </ul>
    <a
      href="/getpdf?save=200&amp;spend=400&amp;timetogoal=32&amp;goal=7000"
      ><button class="displayButton">Download File</button>
    </a>
    <button
      style="margin-left: 5px"
      id="save-budget-button"
      class="displayButton"
    >
      Save Budget
    </button>
  </div>
  <div style="width: 49%; float: right; border: 1px solid #000">
    <h1 class="hformDisplay">Your Budget</h1>
    <form>
      <div
        style="
          width: 49%;
          float: left;
          padding-bottom: 5%;
          padding-top: 6%;
          border-right: 1px solid black;
        "
      >
        <br />
        <label class="textLabelDisplay" for="month">Goal</label><br />
        <br />
        <br />
        <label class="textLabelDisplay" for="monthPay">To Save</label><br />
        <br />
        <br />
        <label class="textLabelDisplay" for="savings">To Spend</label><br />
        <br />
        <br />
        <label class="textLabelDisplay" for="spending">Time Until Goal</label
        ><br />
        <br />
      </div>
      <div style="width: 49%; float: right; margin-bottom: 5%; padding-top: 5%">
        <br />
        <label class="displayLabel">$7000</label><br />
        <br />
        <br />
        <label class="displayLabel">$200</label><br />
        <br />
        <br />
        <label class="displayLabel">$400</label><br />
        <br />
        <br />
        <label class="displayLabel">32 months</label>
        <br />
      </div>
    </form>
  </div>
</div>

<script type="text/javascript" src="/static/saved.js?4c0ac62a"></script>
 </div>
  </body>
</html>'''

SAVED_BUDGETS_PAGE_TEST_DATA = '''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
  <div style="float: left">
    <h1>Your Budgets</h1>
  </div>
  <div style="float: right">
    <button class="displayButton">Toggle Filter Type</button>
  </div>
</div>
<div 
  class="saved_budget_list" 
  id="saved_budget_list"
</div>

<script type="text/javascript" src="/static/packed.js?f7d077a6"></script>
 </div>
  </body>
</html>'''

def make_dashboard_budget_input_data() -> list:
    '''
    Small helpter function that creates test data with the current data.

    Returns:
      list: A list containing to dictionaries of sample budget data.
    '''
    return [
    {'goal': 9000, 'date': datetime.strftime(datetime.now(timezone.utc), '%Y-%m-%d')},
    {'goal': 7000, 'date': datetime.strftime(datetime.now(timezone.utc), '%Y-%m-%d')}
    ]

DASHBOARD_PAGE_TEST_DATA = f'''<!DOCTYPE html>
<html>
  <head>
    <title>Budget Generator</title>
    <link
      rel="stylesheet"
      href="/static/home/main.css"
    />
  </head>
  <body>
    <header>
      <div class="container">
        <strong
          ><nav>
            <ul class="menu">
              <li>
                <a class="link" href="/form"
                  >Quick Budget</a
                >
              </li>
              <li>
                <a class="link" href="/dashboard"
                  >Home</a
                >
              </li>
              <li>
                <a class="link" href="/about">About</a>
              </li>
            </ul>
          </nav></strong
        >
      </div>
    </header>
    <div class="container">
<div class="welcome">
	<h1>Welcome</h1>
	<div class="dashboard-container">
		<div 
			style="
				float: left;
				margin-left: 10px;
				width: fit-content;
			"
			>
			<label>Recent Budgets</label>
			<div
				class="saved-budgets-preview"
				id="saved-budgets-preview"
			>
			</div>
		</div>
		<div
			style="
				width: 225px;
				float: left;
				margin-left: 100px;
				margin-right: 50px;
				padding-top: 100px;"
			>
			<a href="/form"><button style="width: 190px; margin-bottom: 50px;" class="displayButton">Make budget now</button>
 			</a>
			<a href="/saved-budgets"><button style="width: 190px;" class="displayButton">View all budgets</button></a>
		</div>
		<div
			style="
				width: 310px;
				min-width: 200px;
				float: right;
				margin-right: 25px;
				text-align: left;"
			>
			<p>Welcome to your dashboard! Here you are able to view previous budgets at a glance, create a new budget, or view all of your budgets from the saved budgets page! Our high tech systems calculate your budget precisely based on the needs of the individual. We pride ourselves on being the best free budget generator on the net! all you need to do is input a handful of values about your current budget status and we will do the rest for you! Now you can finally rest easy knowing that your budget is in safe hands, possibly the safest hands it has ever been in!</p>
		</div>
	</div>
</div>

<script type="text/javascript" src="/static/dash.js?fffa6eb3"></script>

<script type="text/javascript">displayRecentBudgets({make_dashboard_budget_input_data()})</script>
</div>
  </body>
</html>'''
