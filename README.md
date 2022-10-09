# Robohacks

Created for MLH's RoboHacks II.

## Description

Our website suggests personalized song recommendations based on the mood of a paragraph you submit. Upon submission, the website displays the Spotify tracks for you to listen to.

## Aim
We were inspired by music's ability to convey emotions beyond just words, so we created a website that helps us express ourselves in terms of music. 

## Technologies
Flask, text2emotion library, Spotify API

## Requirements


### Languages
Python, Javascript, HTML, CSS


### Python libraries
- text2emotion: version 0.0.5
- emoji: version 0.6.0
- nltk: version 3.7
- flask: version 2.0.2

## How we built it
We used the Python text2emotion library to assign the mood of a paragraph with five scores from the five emotions of happy, sad, anger, fear, and surprise. We then created an algorithm to correspond the emotions with Spotify track properties (such as loudness, valence, etc.) using Spotify's API. The backend was mainly built with Flask.

## Roadmap
We would like to implement our current features as part of a larger social media app, where users are able to share photos and text simultaneously with music.

## Authors
Arjun Sodhi: Mainly Backend Dev, UX/UI Wireframing/Prototyping, Algorithm Creation

Cindy Li: Mainly Frontend Dev, UX/UI Design, Algorithm Creation
