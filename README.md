<h1 align="center">
  <br>
  <i>Music4Mood</i> by <a href=https://github.com/asterbot>@asterbot</a> and <a href=https://github.com/cindehaa>@cindehaa</a>
  <br>
</h1>

<h4 align="center">A web application that suggests personal song recommendations based on the mood of your inputted paragraph.</h4>

<p align="center">
  <a href="#description-and-aim">Description and Aim</a> •
  <a href="#languages-tools-and-technologies">Languages, Tools, and Technologies</a> •
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#authors">Authors</a>  
</p>

## Description and Aim
This projected was created for MLH's RoboHacks II. Our website suggests personalized song recommendations based on the mood of a paragraph the user submits. Upon submission, the website displays a tailored list of suggested Spotify tracks.

###### To match the song suggestions to the user's mood, we first used the Python text2emotion library to assign the mood of a paragraph with five scores from the five emotions of happy, sad, anger, fear, and surprise. We then created an algorithm to correspond the emotions with Spotify track properties (such as loudness, valence, etc.) using the Spotify API. 

## Languages, Tools, and Technologies
### Languages
Python, Javascript, HTML, CSS

### Back-end Framework
Flask: version 2.0.2

### Python libraries
* text2emotion: version 0.0.5
* emoji: version 0.6.0
* nltk: version 3.7

## Features
* Identifies user's mood along the five dimensions of happy, sad, anger, fear, and surprise
* Tailored song recommendations based on the user's mood
* Customize the number of song recommendations displayed, with up to 21 maximum song recommendations
* Visually appealing UI, with: 
  *  Animated text upon loading the website
  *  Buttons and textbox that change state upon hover and click
  *  Adjustment of website elements based on screen size 

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com), [Python](https://www.python.org/downloads/), and an IDE.

###### Note that the Spotify Access token may be outdated. Please check step 4 if you receive an Internal Server Error.

1. From the terminal, clone the repository:
git clone https://github.com/asterbot/Music4mood

2. Install Flask and the following libraries: text2emotion, emoji, nltk
* python -m pip install flask
* python -m pip install text2emotion
* python -m pip install emoji
* python -m pip install nltk

3. Run main.py. Click around the text to input text in a textbox. Use the slider to select the number of songs you wish to be suggested. Click on "Find me songs!" to receive a custom list of song recommendations on the next page.

4. If you receive an Internal Server Error, a new access token may be needed. Log onto developer.spotify.com, and navigate to [Console](https://developer.spotify.com/console/) -> Browse -> [Get Recommendations](https://developer.spotify.com/console/get-recommendations/). Scroll down to OAuth Token and click on "Get Token", then "Request Token". Copy the OAuth Token and replace the access token in line 8 of main.py with the OAuth Token.

## Roadmap
We would like to implement our current features as part of a larger social media app, where users are able to share photos and text simultaneously with music.

## Authors

Arjun Sodhi: Mainly Back-end Dev, UX/UI Wireframing/Prototyping, Algorithm Creation

Cindy Li: Mainly Front-end Dev, UX/UI Design, Algorithm Creation, README.md

---
> GitHub [@asterbot](https://github.com/asterbot) &nbsp;&middot;&nbsp;
>  LinkedIn [@arjun-sodhi](https://www.linkedin.com/in/arjun-sodhi/) 

> GitHub [@cindehaa](https://github.com/cindehaa) &nbsp;&middot;&nbsp;
> LinkedIn [@cindehaa](https://www.linkedin.com/in/cindehaa/)
