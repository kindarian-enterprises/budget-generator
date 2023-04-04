# Budget Generator

A small web app for making budgets

## Description

This app creates simple budgets for the user and allows the budgets to be saved or downloaded. At the moment, there

is no ability to log in, but that feature is planned to be added in the future.

## Motivation

My motivation for making this app was to work with python and flask and learn various packages relating to web applications

and working with a database. I also am using this app as an opportunity to learn about containerization through docker and docker-compose.

## Testing And Deployment

Under github/workflows directory, there are two different actions at the moment. One action is set up to run my tests on pull requests to master as well as

generate a coverage file to ensure that the test coverage is at least 80% before allowing the code to be merged.

The other action file waits for a pull request to main to be closed, and then runs a build script that creates a new image of the app and pushes it up to docker hub

## Methodology

The UI of the application does not look amazing, and the functionality is not very impressive either, however, I have used this application as an opportunity to learn about the software development life cycle. From planning out what I wanted the app to do,
to creating task tickets, every step of the way was first planned thoroughly before execution.

### Planning

When the idea was first thought of to make this app, here are the steps I took:

- Planning out using user stories to figure out exactly what I wanted the functionality of the app to be.
- Using these user stories to identify different what could be set as milestones for different versions of the app.
- Creating mocks of each necessary page using draw.io to give me a starting point.

### Execution

After the planning phase was over, I broke up the work for version one into tasks using Trello and github projects

in order to make clear targets and goals for the foreseeable future. I used some basic concepts from agile development to create a workflow which would both help me effectively implement these tasks as well as help me begin to learn about a few core tenants of agile development. These pieces of the workflow were:

- Having an async standup with my mentor every morning talking about what I had done yesterday and was going to do today.
- Having pre-defined tasks that I get done over the course of a 4 - 7 day period.

Throughout this process, I began to learn about some methods of how to architect an application, as well as gained familiarity with Flask and Python. Using Flask, I created API endpoints that would serve to either display my HTML pages or generate/save budgets.

### Versioning

This project is still in development and there are future plans to turn it into a single page application using React for the front-end and having my Flask application serving CRUD endpoints.
