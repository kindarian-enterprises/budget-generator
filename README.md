# Budget Generator

A small web app for making budgets

## Description

This app creates simple budgets for the user and allows the budgets to be saved or downloaded. At the moment, there
is no ability to log in, but that feature is planned to be added in the future.

## Building and Usage

In order to use the app all you have to do is make sure docker and docker compose are on your system, then pull the docker image from docker hub using the command

    docker pull edisonstuart/budget-generator

After you have pulled the image down, you can run it using the docker-compose.main.yaml file from the repo with the command

    docker-compose -f docker-compose.main.yaml up

I like the run it as detached with the -d flag because that way you can still use your terminal window. After that, the application should be running on your localhost!

## Motivation

My motivation for making this app was to work with python and flask and learn various packages relating to web applications and working with a database. I am also using this app as an opportunity to learn about containerization through docker and docker-compose.

## Testing and Deployment

Under the github/workflows directory, there are two different actions at the moment. One action is set up to run my tests on pull requests to master as well as generate a coverage file to ensure that the test coverage is at least 80% before allowing the code to be merged.
The other action file waits for a pull request to main to be closed, and then runs a build script that creates a new image of the app and pushes it up to docker hub

## Methodology

The UI of the application does not look amazing, and the functionality is not very impressive either; however, I have used this application as an opportunity to learn about the software development life cycle. From planning out what I wanted the app to do, to creating task tickets, every step of the way was thoroughly planned before execution.

### Planning

When the idea was first thought of to make this app, here are the steps I took:

- Planning out using user stories to figure out exactly what I wanted the functionality of the app to be.
- Using these user stories to identify different things that could be set as milestones for different versions of the app.
- Creating mockups of each necessary page using Draw.io to give me a starting point.

As an example, here are some of the user stories that I created in order to understand exactly what I wanted to do:

User 1: I want to create a budget without having to create an account.

- I open my browser and head to the budget website.
- I navigate to the quick budget option.
- I enter my information about the budget i want created.
- I submit the budget and get a readout of my info.
- I press the download as file button and get it returned to me as a downloadable file.
- I exit the page and now have my budget file.

User 2 (Filtered budgets view): I want to view and download certain budgets that I have created.

- I open my browser and head to the budget website.
- I hit login and enter my info.
- I am routed to the account dashboard and select the view all budgets button.
- I then can filter the budgets (possibly based on date created or urgency).
- I log out of the account and exit the browser.

These user stories, along with mocking my webpage layout, helped me very clearly define what it was I wanted to accomplish and made it easier to take small steps to get this functionality working.

### Execution

After the planning phase was over, I broke up the work for version one into tasks using Trello and Github projects in order to make clear targets and goals for the foreseeable future. I used some basic concepts from agile development, such as:

- Having a working application with added functionality at each step of the build process.
- Having an async standup with my mentor every morning, talking about what I had done yesterday and was going to do today.
- Having pre-defined tasks that I get done over the course of a 4 - 7 day period.
- Responding to change throughout the process, such as switching to a new PDF generation package for versioning purposes.

These concepts allowed me to create a workflow that would both help me effectively implement the tasks I set out to do as well as help me begin to learn about a few of these core tenets of agile development.
Throughout this process, I gained familiarity with Flask and Python. Using Flask, I created API endpoints that would serve to either display my HTML pages or generate/save budgets.

### Versioning

For the versioning of the application, I split up the plans I had for it into some steps for a road map. Here is a piece of the road map up until version 2:

- First iteration v1.0
  -- Quick budget generator w/file download option
  -- Automated tests for our code
  -- Tests can be run locally (pytest or similar)
  -- Repo-level: use github actions to run automated tests on our branches
  -- Create some github actions
  -- Deployment solution: application will be containerized
  -- Docker containers - Start off with docker-compose: we can launch our app on an env with only docker and docker compose installed, using our docker-compose script

- Second iteration v2.0
  -- Multi-user app
  -- Ability to save and recall previously created budgets
  -- Considerations:
  1.  What kind of data? What is its structure? What type of DB shall we use?
  2.  How do we do auth(orization) and (entication)?

This project is still in development, and there are future plans to turn it into a single page application using React for the front-end and having my Flask application serving REST endpoints.
