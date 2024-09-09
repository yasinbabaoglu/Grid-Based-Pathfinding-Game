# Grid-Based Pathfinding Game with A* Algorithm

This project is a grid-based strategy game implemented in Python using Pygame. It features A* pathfinding algorithms for game characters and requires the player to navigate the grid to reach a goal while avoiding obstacles. The player competes against a computer-controlled opponent, each trying to reach their goal first or cause the other to lose.

## Features

- *A Pathfinding Algorithm*: The game uses the A algorithm for calculating optimal paths for the computer-controlled character.
- *Dynamic Gameplay*: The player and computer character navigate a grid full of obstacles, dynamically updating paths as they move.
- *Graphical User Interface*: The game uses Pygame to display the game grid, obstacles, and movements of the player and computer characters.
- *Win and Lose Conditions*: The game checks for win/loss conditions when the player or computer reaches the goal or collides with obstacles.

## Prerequisites

Before running the game, ensure you have Python installed along with the required libraries:

1. [Python](https://www.python.org/downloads/) (version 3.7 or higher recommended)
2. Required Python libraries:
   - [Pygame](https://www.pygame.org/news)
   
You can install Pygame using pip:

bash
pip install pygame


## How It Works

### Gameplay

1. The game initializes a grid where the player (O), computer (B), and obstacles (C) are randomly placed.
2. The player uses arrow keys to move up, down, left, or right on the grid.
3. The computer character uses the A* algorithm to navigate toward its goal, avoiding obstacles dynamically.
4. The player wins by reaching the goal (H) first, and the computer wins by reaching the goal or causing the player to get stuck or hit obstacles.

### A* Algorithm

- The A* algorithm is implemented to calculate the shortest path from the start to the goal, considering obstacles.
- Both the player and computer characters have their pathfinding logic based on grid constraints.

## Running the Game

1. Ensure all scripts (a_star.py, game_lib.py) are in the same directory.
2. Run the game_lib.py script to start the game:

   bash
   python game_lib.py
   

3. Control your character using the arrow keys:
   - *Up Arrow*: Move up
   - *Down Arrow*: Move down
   - *Left Arrow*: Move left
   - *Right Arrow*: Move right
   - *R Key*: Restart the game

4. Try to reach the goal (H) before the computer-controlled character.

### Game Setup and Initialization

- The grid size is set to 20x30 by default.
- The player (O) starts at the bottom-left corner, and the computer (B) starts at the top-left corner.
- The goal (H) is set in the middle of the right side of the grid.
- Random obstacles (C) are placed around the grid but ensure a path is available for both player and computer to reach the goal.

## Key Classes and Functions

### Oyun Class (Game Logic)

- **init()**: Initializes the game grid, sets initial positions for the player, computer, and goal.
- **game_loop()**: Main loop that captures user input and updates the game state.
- **computer()*: Controls the computer character's movement using the A algorithm.
- **draw_numbers()** and **draw_background()**: Handles drawing the grid and updating the display.

### a_star.py Module

- **a_star()*: Implements the A algorithm to calculate the path for the computer or player character.
- **calculate_estimate()**: Estimates possible movements based on the current position and obstacles.
- **calculate_move()**: Determines the next move for the character based on the calculated path.
