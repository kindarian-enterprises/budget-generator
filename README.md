# Budget Generator
A small web app for making budgets

## Description
This app creates simple budgets for the user and allows the budgets to be saved or downloaded. At the moment there
is no ability to log in but that feature is planned to be added in the future.

## Motivation
My motivation for making this app was to work with python and flask and learn various packages relating to web applications
and working with a database. I also am using this app as an opportunity to learn about containerization through docker and docker-compose.

## Testing And Deployment
Under github/workflows directory there are two different actions at the moment. One action is set up to run my tests on pull requests to master as well as
generate a coverage file to ensure that the test coverage is at least 80% before allowing the code to be merged.

The other action file waits for a pull request to main to be closed, and then runs a build script that creates a new image of the app and pushes it up to docker hub
