# NFL Play by Play Data Analysis

## General Info
* Timmy Sullivan, tps7@illinois.edu (team captain)
* Team Name: Group 268
* Code Repo: https://github.com/tps7/CS410Project
* Project Video: TBD

## Project Overview
The goal of my project was to find NFL play by play data online and parse the play by play data to get statistical data on the players in that play. Having this data would allow me to calculate custom statistics that can't be found online. The main purpose of this is for analysis in fantasy football and general statistical discovery.

## Project Implementation
### Data sources
Play by play data: https://nflsavant.com/about.php (pbp-2022.csv)\
Fantasy player data: https://www.fantasypros.com/nfl/reports/leaders/ppr.php?year=2022 (player_2022_season.csv) \
Weekly schedule: https://www.pro-football-reference.com/years/2022/games.htm (2022_week_date_data.csv)
### Software Implementation
There are 6 main files that I used to implement my code. \
player.py: This file contains the player class. I designed my project in a way that each player is its own object. Each player object contains all the data on itself for every week in the season (i.e. yards, touchdowns, fantasy points). \
stats.py: This is another class that holds statistical data for a single week for a player. 
play.py: This is another class that is just an object for each piece of play by play data. It holds all the important statistics for each play for a particular player.\
project.py: This file is where I actually do most of my work. In this file I get all the player data and actually go through and parse the play by play data, calulating statistics for every player. ]
test.py: In this file I have test cases to ensure my parser is extracting the data properly. analysis.py: This file is where I actually calulate statistics. Currently I have 5 functions as examples, but a user can easily add more. All statistics calculated here are written to the out.txt file. 

## Project Setup
I run my project using python and pandas. I spefically am using python 3.8.17 and pandas 2.0.3, but older or newer versions of both should be able to run my code as well. \
The instructions for setup are below:
1. Clone from github repo "git clone https://github.com/tps7/CS410Project.git"
2. Install python and pandas if not already installed. There are plenty of tutorials online explaining how to do this if you are having trouble.
3. Open the cloned files in an editor of your choice (I like to use VS Code)
4. Run analysis.py. Can do this in terminal with "python analysis.py, or in an editor of your choice."
5. The output should print to the file out.txt. From here you can use the data that has already been parsed to write functions of your own to calulate more statistics, or you can run the five example files I already implemented. 


## Project Self Reflection
I am very happy with the way my project turned out. My project ended up being a lot more complicated than I was expecting. Working with a dataset of ~40,000 plays I knew there were going to be some edge cases, but I underestimated how many edge cases there would be and how specific each edge case would be. Partially through my project I realized that obtaining 100 % accuracy on my parser was unrealistic. Instead of going for 100 % accuracy I decided that an accuracy in the high 90's was good enough. My goal was to get more general takeaways from these statistics, so small variance in player statistics won't change the overall takeaways (i.e. A player may move one or two spots up or down, but overall the player will either be in the towards the top or towards the bottom, so the general takeaways will be the same). I spent well over 20 hours on this project (~30 hours), so without shifting my goal away from 100 % accuracy I don't think I would have been able to deliver as good of a finished product. 
