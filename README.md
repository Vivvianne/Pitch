# A minute pitch App

Author: Vivvianne Kimani

## Description

This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

##User Stories

* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.

## BDD

| Behavior | Input | Output |
|:---------|-------|--------|
|signup/login field| Input credentials | A welcoming message |
| Display Various Pitch Categories | N/A | Various pitches grouped by category are displayed |
| Add category | Input a category | Inputed category dispalyed |
| Add new pitch | Click New pitch | New pitch added |
| Display pitches | Click on a Category | A page with a list of pitches from the selected category |
|  View Pitches | Click on a pitch | View a pitch and comments |
| Comment on a pitch | Click Comment | Registered User displays a form where a user can comment on a certain pitch |

##  Prerequisites
* Python3.6
* Flask
* Postgresql

## Setup/Installation Requirements
* Internet access
* $ git clone https://github.com/kepha-okari/one-minute-pitch.git
* $ cd one-minute-pitch
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh

## How the app works
A user needs to sign up
A user the needs to sign in to vote and post pitches

## Live link
You can view the project from here https://pitchput.herokuapp.com/

## Contacts
For further questions you can send an email to ndiahav@gmail.com

## Technologies used 

* Python3.6
* Flask framework
* Bootstrap
* PostgreSQL

## License

MIT (c) 2019 https://github.com/Vivvianne/Pitch/blob/master/LICENSE
