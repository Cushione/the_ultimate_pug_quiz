# The Ultimate Pug Quiz

Pugs have captured the hearts of millions around the world. Known for their cheerful attitude, moderate exercise needs, and loving nature, pugs make wonderful companions for people of all ages and circumstances.
If you're a true pug lover, you can test your knowledge with this medium difficulty quiz that has 10 questions and is bound to bring some fun into your life.

# Video Demo

[![The Ultimate Pug Quiz Demo](https://img.youtube.com/vi/Gk7mGUqbszQ/0.jpg)](https://www.youtube.com/watch?v=Gk7mGUqbszQ)

# Live Page

This quiz is online on Render and can be accessed by the following link:
[The Ultimate Pug Quiz](https://the-ultimate-pug-quiz.onrender.com/)

# Objective

This project is my final work for CS50 Introduction to computer science course at Harvard University. I have developed this project using Django and Tailwind and thus demonstrated my coding skills, while creating a functional, fun website.

# Contents

- [Features](#features)
  - [Additional Features](#additional-features)
  - [Bugs](#bugs)
- [Files](#files)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Used Technologies and Tools](#used-technologies-and-tools)
  - [Django Apps](#django-apps)
- [Acknowledgments](#acknowledgments)

# FEATURES

The landing page is a simple introductury page from where you can access a new game or you can continue an existing game.
Once starting a quiz, you have to answer 10 different questions about pugs. After submitting an answer, you are immediatelly informed if your choice was correct or not. At the end of the quiz, you receive your score on the result page. Then you can either choose to start a new game or return to a home page.

## Additional Features

Features that could be implemented in the future:

- Allow visitors to log in and create a profile where they can see past games

## Bugs

There are no known unfixed bugs.

# Files

## pug_quiz
This module is the root Django app.

### settings.py
This files contains all the Django settings such as the list of installed apps and the database config.

### urls.py
This file contains the list of available urls in the application. It defines the url for the admin panel and includes all the urls from the the quiz app.

## quiz
This module is the app that contains all the files for the quiz application.

### migrations
This folder contains all the migration files for the database.

### templates
This folder contains the html templates for the three pages: Home, Quiz and Result.

### admin.py
This file registers the custom model in the Django admin panel where they can be created, read, updated and deleted

### forms.py
This file contains the form structure for the answer POST method. It defines a single field answer as an integer field.

### models.py
This file defines the database models of the application. It contains three models: Game, Question and Answer. It also defines the structure of the pivot table for the many-to-many relationship of the Game and Question models.

### urls.py
This file contains the urls for the quiz. It defines four urls: Homepage, New Game, Game and Result. The urls are then included in the root apps url file.

### views.py
This file defines the views or logic for the four available urls.

#### HomeView
This view only checks if a game is in progress and then renders the "home.html" template.

#### start_new_game
This method is used for both POST and GET requests. It finishes any running game and then creates a new one. Afterwards, it redirects the user to the game view

#### GameView
This view has two methods, one for GET requests and one for POST requests.
For the GET requests, it loads the game with the uuid defined in the url and then finds the next unanswered question in that game. If the game has an unanswered question, it renders the "quiz.html" template with that question. If the game has no unanswered questions, the user is redirected to the result view.
For the POST requests, it also loads the game defined in the url and then checks if the body of the POST request has the correct format. If the format is correct, i.e. the user sent only the id of the selected answer, the view checks if the answer is correct and updates the row in the database accordingly. Then the "quiz.html" template is rendered that shows the user if his answer was correct.

#### ResultView
This view only loads the game with the uuid defined in the url and then renders the "result.html" template that displays the achieved score for that game.

# Deployment

The site was deployed using Render.
The live link can be found here: [The Ultimate Pug Quiz](https://the-ultimate-pug-quiz.onrender.com/)

# Credits

## Used Technologies and Tools

- [Django](https://www.djangoproject.com/) - As the project framework
- [Tailwind](https://tailwindcss.com/) - As the CSS framework
- [Render](https://render.com/) - For the deployment of the website

## Django Apps

- [django-tailwind](https://pypi.org/project/django-tailwind/) To integrate Tailwind into Django
