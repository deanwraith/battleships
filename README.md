# Battleship Game Game
![Battleship](assests/images/shutterstock_1252263685.png)
https://github.com/deanwraith/battleships

Battleships is a strategy game played between two players each with a board that has a coordinate grid on it. Each player randomly places their ships on the board and the players take turns selcting positions trying to find their opponents ships. When one player has found all the other players ships and sunk them first they are the winner.

# Table of Contents

- [How to use the app](#how-to-use-the-app)
- [Features](#features)
    * [Game Features](#game-features)
- [Testing](#testing)
    * [Validation Testing](#validation-testing)
    * [Bugs](#bugs)
- [Developement Cycle](#developement-cycle)
    * [Commit Diary](#commit-diary)
- [Technology Used](#technology-used)
- [Deployment](#deployment)
- [Credits](#credits)
    * [Content](#content)

## How to use the app
When the user first opens the app they are greated and asked for a user name. Once a username is selected the user and computers ships are randomly placed on the board and the user is prompted to make their first move.

A turn consists of the user selecting a row and comlumn each an integer between 1 and 8. When the user has made their selection they will be prompted whether the selection was a hit or a miss. Then the computer has a turn and the result is posted.

The user has 20 moves to try and sink the computers 10 ships. If either the user or computer sink all 10 ships before the moves are all used they are the winner. If neither player sinks the 10 ships in the 20 moves the game is a draw and can be restarted.

[Back to Table of Contents](#table-of-contents)

## Features

### Game Features
* The game is unique to each user by the username.

* The program randomly places both players ships on each of their boards.

* The game will run the input to check if it is a hit or a miss. It will also check if the input has been used before or not on the game board. The appropriate message is displayed for the outcome.

* The program keeps count of the number of moves played and number of ships sunk and has a counter to keep the user on track with how many moves played.

* A message will be displayed at the end of the game to inform the user who has won or if they have run out of moves and the game is a draw.

[Back to Table of Contents](#table-of-contents)

## Testing

### Game
| Function | Description | Result |
| --- | --- | --- |
| Username request | Username saved and posted when game starts | Passed |
| User input| User inputs an integer for row and column and is run | Passed |
| User input errors | Message displayed when user input is incorrect | Passed |
| Move counter | Counter adjusts with each move | Passed |
| Hit or Miss check | Check if input is a hit or miss | Passed |
| Computer move | Computer move after user move | Passed |
| Win or lose | Number of ships sunk or moves used up for win, loss or draw | Passed |

[Back to Table of Contents](#table-of-contents)

### Validation Testing
* Python
    * [PEP8](http://pep8online.com/)
    All Python code was checked using this validator and was returned without any issues.

### Bugs
* Any bugs

[Back to Table of Contents](#table-of-contents)

## Developement Cycle
### Commit Diary
    * 19:05 19/02/2022 - Added structure and function

    * 19:15 19/02/2022 - Added functionality to place ships

    * 19:32 19/02/2022 - Generated welcome message and instructions

    * 19:53 19/02/2022 - Added game functionality

    * 21:34 19/02/2022 - Corrected code and notes

    * 23:06 19/02/2022 - ReadME.md file edited
    
[Back to Table of Contents](#table-of-contents)

## Technology Used

* Github
* Gitpod
* Heroku
* Python

## Deployment

The site has been deployed using Heroku.

* The Github repository was linked to the Heroku app generator.
* The settings were adjusted to match the required requirements.

* The game was then live and can be found at https://battleshipsdean.herokuapp.com/

[Back to Table of Contents](#table-of-contents)

## Credits

### Content
    * Code Institute Python Template
    * W3Schools - Used the resources as a guideline for various functionality and styling.

[Back to Table of Contents](#table-of-contents)