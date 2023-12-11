# NFL Play by Play Data Analysis

## General Info
* Timmy Sullivan, tps7@illinois.edu (team captain)
* Team Name: Group 268
* Code Repo: https://github.com/tps7/CS410Project
* Project Video: https://drive.google.com/file/d/12-yZfghNUS0bDaqdhkXZNcJVfBT5Mcde/view?usp=sharing

## Project Overview
The goal of my project was to find NFL play by play data online and parse the play by play data to get statistical data on the players in that play. Having this data would allow me to calculate custom statistics that can't be found online. The main purpose of this is for analysis in fantasy football and general statistical discovery.

## Project Implementation
### Data sources
Play by play data: https://nflsavant.com/about.php (pbp-2022.csv)\
Fantasy player data: https://www.fantasypros.com/nfl/reports/leaders/ppr.php?year=2022 (player_2022_season.csv) \
Weekly schedule: https://www.pro-football-reference.com/years/2022/games.htm (2022_week_date_data.csv)
### Software Overview
There are 6 main files that I used to implement my code. \
player.py: This file contains the player class. I designed my project in a way that each player is its own object. Each player object contains all the data on itself for every week in the season (i.e. yards, touchdowns, fantasy points). \
stats.py: This is another class that holds statistical data for a single week for a player. 
play.py: This is another class that is just an object for each piece of play by play data. It holds all the important statistics for each play for a particular player.\
project.py: This file is where I actually do most of my work. In this file I get all the player data and actually go through and parse the play by play data, calculating statistics for every player. \
test.py: In this file I have test cases to ensure my parser is extracting the data properly. analysis.py: This file is where I actually calculate statistics. Currently I have 5 functions as examples, but a user can easily add more. All statistics calculated here are written to the out.txt file. \
More details on each of these files and the functions included within them are included in the code documentation within the files. 
## Project Setup
I run my project using python and pandas. Specifically I am using python 3.8.17 and pandas 2.0.3, but older or newer versions of both should be able to run my code as well. \
The instructions for setup are below:
1. Clone from GitHub repo "git clone https://github.com/tps7/CS410Project.git"
2. Install python and pandas if not already installed. There are plenty of tutorials online explaining how to do this if you are having trouble.
3. Open the cloned files in an editor of your choice (I like to use VS Code)
4. Run analysis.py. Can do this in terminal with "python analysis.py, or in an editor of your choice."
5. The output should print to the file out.txt. From here you can use the data that has already been parsed to write functions of your own to calculate more statistics, or you can run the five example files I already implemented. 

## How to use
Once you get the project set up using the project is simple all you need to do is run analysis.py and it will output statistics in the file out.txt. Right now I only have five sample calculations included, however if a user wants to calculate different stats, for example what QB converted the most 3rd down's from 10+ yards away in 2022, the user would need to write another function to do that. This wouldn't be too hard as it would be very similar to the other functions I already wrote in terms of structure. 

## Project Reflection
I am very happy with the way my project turned out. I definitely met my goal of being able to calculate advanced statistics from the NFL play by play data. There is however one goal I did not meet. I was unable to achieve 100 % accuracy on my parser in my test cases. This is due to me underestimating the number of edge cases I had to deal with in the project. There are ~40,000 plays in the play by play data, and I estimate there is about 50 very specific edge cases that are causing the errors. By very specific I mean an edge case that only effects one or two plays the entire season. I have very high accuracy on my test cases (upper 90's), so I decided to let those extremely specific edge cases slide and put more focus on the other aspects of my project. The main reason I did this is because I don't think missing a couple of plays will have any impact on general takeaways from my statistics.  (i.e. A player may move one or two spots up or down, but overall the player will either be in the towards the top or towards the bottom, so the general takeaways will be the same). Other than this one issue the rest of the project was great. I implemented five example use cases to demonstrate the types of statistical analysis that can be done using the play by play data. \

If anyone has any questions, or they are having trouble accessing or using parts of my project please reach out to me at tps7@illinois.edu. 


