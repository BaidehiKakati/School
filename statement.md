Guess The Number – Python Number Challenge

_________________________________________________________________________________

1. PROBLEM STATEMENT
Learning Python programming can be challenging and intimidating for a beginner when concepts are discussed in theoretical aspects. Students require applications where they can apply the learned concepts like variables, conditional statements, loops, functions, random number, input validation, and modular programming.

Guess The Number– Python Number Challenge is a python console application that provides an interactive platform to implement the python programming concepts.

The game is designed in such a way that the computer picks a secret number and the player guesses the number with limited attempts.

The game provides hints, calculates scores, and maintains a scoreboard. The game provides various difficulty levels for enhanced experience.

_________________________________________________________________________________

2. Scope of the Project
Guess The Number– Python Number Challenge is a scope of building a python interactive console game that provides an insight into the python programming language. It is a fun-filled and exciting way to learn python.

The scope of the application consists of:

•	Display the name of the game and rules of the game.

•	Take the input of the player’s name.

•	Provide multiple difficulty levels.

•	Display the random computer pick number.

•	Allow the player to make guesses within the limited attempts.

•	Provide higher/lower hints to the player.

•	Calculates the player score.

•	Maintain a scoreboard during the session.

•	Take input from the user.

•	Handle invalid input from the user.

•	Perform unit testing for major modules and components using the python “unittest” framework.

The application will not require external libraries as of now. The console application will be built-in using the Python language.


3. Target Users for the Game

The target users for Guess The Number – Python Number Challenge are as follows:

1. Python beginners – A python beginner is a student who has begun studying the fundamentals of Python programming.

2. College students – A college student refers to someone who is attending a university or college and enrolled in courses.

3. Programming learners – A programming learner is someone who learns to create software or web applications.

4. Casual users – A casual user is someone who uses a service or software not to work or make money.

_________________________________________________________________________________

4. High- Level Features of the game
    4.1 Game Introduction 
    The game will start by displaying the project 
       name “CODEQUEST – PYTHON NUMBER 
      CHALLENGE”.   
      4.2 Player Registration
      The rules of the game will be displayed before the 
      game starts.
      The game will take input of the Player Name and 
      proceed with the game.
      4.3 Difficulty Level
       The game will provide 3-level difficulty:
•	Easy Mode – Computer picks a secret number from 1 
                    to 50
•	Medium Mode – Computer picks a secret number from 1 to 100

•	Hard Mode – Computer picks a secret number from 1 to 500
      4.4 Random Number Generation  
         The computer will pick a secret number using the 
      random library.
      4.5 Guessing System
      The player will make guesses until the player finds the   
      correct number or runs out of attempts.
      4.6 Hint System
      The game will provide hints if the player’s guess is not 
      correct.
•	“HIGHER” – if the guess is lower than the secret number.
•	“LOWER” – if the guess is higher than the secret number.
      4.7 Scoring System
      The player will get a score on getting the correct 
      number.
      Scores are based on difficulty levels and attempts.
      4.8 Scoreboard
      The game will save the rounds result in the scoreboard.
      The scoreboard contains the player name, difficulty 
      level, score, and attempts.
      4.9 Input Validation
      The game will validate the input and make sure it does 
      not break the application.
      4.10 Testing
      The application will have a testing file, test_game.py.   
      This file will test crucial application features like adding 
      a player, negative scores, and scoreboard records.
      The game will have assertions to test whether the 
      scoreboard adds records correctly and if the records 
      are sorted in the correct order.

5. Project Moduele
The game divides the files into different modules for better organization.

Guess The Number_VITyarthi/
├ main.py

├ game.py

├player.py

├ scoreboard.py

├ utils.py

├ test_game.py

├ README.md

└── statement.md

Each module serves a unique purpose in the application.

 Module  Description 
•	main.py --- Starts the application 
•	game.py --- Holds the logic of the game 
•	player.py--- Holds the logic for the player
•	scoreboard.py--- Logic for the scoreboard
•	utils.py--- Utility functions for the game 
•	test_game.py---Unit testing for the application
•	README.md--- Application instructions
•	statement.md--- Project scope and overview

6. Technologies Used in Th Game
•	Programming Language – Python
•	Random Number – Python Random
•	ModuleTerminal – OS module
•	Testing – Python unittest module
•	Development Environment – VS Code / Python IDLE / any Python IDE

7. Expected Outcome
The expected outcome is to create a functional Python console game. The application should provide a great user experience and give an insight into the working of the Python programming language. The game will offer an exciting way to learn Python by providing a fun and interactive platform.

The application is expected to allow users to play the game, read the game instructions, choose the game difficulty, guess the number, get hints, score points, and see the scoreboards.
