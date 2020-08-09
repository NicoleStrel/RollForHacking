# RollForHacking
### Functional Features
- Login/Sign in Auth
- The 3 availible games
- Map of friends
- Avatar/ location selection

### Prototypes
- friendslist page
- friends search page
- login as guest
- customize games button
- making groups
- friend invites

## Local Set up
- Clone GitHub repository locally `git clone [repo-link]`
- install dependancies: `pip install -r requirements.txt` (we need this to download packages for google maps, etc)
- `cd rollforhacking`
- make sure you have python3 installed
- set up virtual environment
    - `pip install virtualenv`
    - `virtualenv venv`
- to activate environment: `source venv/bin/activate`
- to deactivate: `deactivate`
- create a `.env` file (same directory as .env.sample) and add the secret key

## Local server start

- `cd rollforhacking` 
- `python manage.py runserver`
