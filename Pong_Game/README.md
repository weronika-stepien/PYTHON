<div align="center">

# Pong Game
#### A two-player game built using the Pygame library


![Preview](/Images/pong.gif)

![Version](https://img.shields.io/badge/version-1.0-blue?style=for-the-badge&labelColor=black) ![Static Badge](https://img.shields.io/badge/3-blue?style=for-the-badge&label=python&labelColor=black) ![Static Badge](https://img.shields.io/badge/windows%20%7C%20macOs%20%7C%20linux-blue?style=for-the-badge&label=platform&labelColor=black) 










------------


![Static Badge](https://img.shields.io/badge/Table%20%20%20%20%20%20%20%20%20%20%20of%20%20%20%20%20%20%20%20%20%20Contents-blue?style=for-the-badge&logoColor=darkviolet)

**| [Overview](#overview) | [Key Features](#key-features) | [User Manual](#user-manual) | [Ongoing Improvements and Known Bugs](#ongoing-improvements-and-known-bugs) | [Found a Bug?](#found-a-bug) |**





------------



## Overview
The minimalistic Pong game implemented in Python using Pygame. It features smooth gameplay, paddle and ball mechanics plus customizable win conditions, all running at a smooth 60 FPS.


------------



## Key Features
##### Paddle Movement Control
###### Players control paddles using the `W` and `S` keys for the left paddle and the arrow keys for the right paddle.
##### Ball Physics
###### The ball moves across the screen, bouncing off the paddles and the walls with realistic velocity changes based on the point of impact.
##### Collision Detection
###### Accurate collision detection ensures the ball bounces off paddles and the screen boundaries appropriately.
##### Real-Time Scorekeeping</center>
###### Tracks and displays the score for both players, showing each player’s progress during the match.
##### Winning Condition
###### The first player to reach the winning score is declared the victor, and a winning message is displayed on the screen.


------------



## User Manual
</div>

####  Requirements
###### Python Version
The game requires `Python 3` or higher to run. You can check your  version by running below command:
```bash
$ python -version
```
###### Pygame library
If you are running the game from source code, make sure `Pygame` is installed and configured. You can check if it is installed by running the following commands in the terminal:
- Method 1 - Checking Installed Packages (Pip)
```bash
# Depending on your system you can either use
$ pip list | grep pygame
# Or
$ pip3 list | grep pygame
```
If `Pygame` is installed, it will appear in the list with its version number.

-  Method 2 - Using the Command Line
```bash
# Depending on your system you can either use
$ python -m pygame --version
# Or
$ python3 -m pygame --version
```
If `Pygame` is installed, this will print the version number of it. If not, you'll see an error saying that the module was not found.

- Method 3 - Using the Python Interpreter
1. Enter the Python interactive shell by typing:
```bash
$ python
```
or, depending on your system:
```bash
$ python3
```
2. Once you're inside the Python shell, type:
```python
$ import pygame
```
3. If `Pygame` is installed, you will not see any output or errors. If it is not installed, you will see an error like this:
```vbnet
$ ModuleNotFoundError: No module named 'pygame'
```
4. To exit the Python shell, type:
```python
$ exit()
```

#### Getting Started
###### To run a program, you need to:
- Clone this repository
 ```bash
$ git clone <repository_url>
```
###### If you're using the executable file:
- Navigate to the repository's `releases` folder where the executable file is located.
- Double-click the executable file (`Pong.jar`) to launch the game.
- If the executable does not open via double-click, run the following command from the terminal/command prompt:
```bash
$  python Pong.jar
```
###### If you're running from Source Code
- Open the project in your preferred  `IDE` (e.g.,PyCharm, IntelliJ IDEA, Eclipse).
- Run the `solution.py` class located in the `venv` package to launch the game.

#### Customization
###### Winning Score
The default winning score is set to `2`, but you can change this to make the game longer or shorter.

**Steps to make the change:**
1. Open `solution.py`.
2. Look for the `WINNING_SCORE` variable at the top of the file:
```python
$ WINNING_SCORE = 2
```
3. Change the value to your desired winning score.

###### Key Bindings
You can customize the keys used to control the paddles by modifying the key events in the `handle_paddle_movement` function.
**Steps to make the change:**
- In the `handle_paddle_movement` function, locate the key bindings for player controls:
```python
$ if keys[pygame.K_w]:
    left_paddle.move(up=True)
$ if keys[pygame.K_s]:
    left_paddle.move(up=False)
```
- Change the `pygame.K_w` and `pygame.K_s` to other keys (e.g., `pygame.K_a`, `pygame.K_z`) if you want different controls for the left paddle.
- Similarly, adjust the key bindings for the right paddle (`pygame.K_UP`, `pygame.K_DOWN`) to new keys as needed.

------------
<div align="center">

## Ongoing Improvements and Known Bugs

| # | Name                         | Type             | Description                                                                                                                     |
|---|------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1 | AI for Single-Player Mode    | Work in progress | Currently working on adding a single-player mode with AI opponents that will scale in difficulty.                               |
| 2 | Leaderboards and High Scores | Work in progress | Developing a system for recording and displaying player high scores and win/loss statistics across multiple rounds or sessions. |





------------

## Found a bug?

If you encounter any issues or bugs while using this project, please feel free to open an issue in the Issues section of the repository. Make sure to describe the bug in detail, providing steps to reproduce, expected behavior, and any relevant logs or screenshots.

If you'd like to contribute a fix for the issue, you're welcome to submit a pull request (PR). When submitting a PR, please reference the issue number and provide a description of the changes made.


------------

</div>





