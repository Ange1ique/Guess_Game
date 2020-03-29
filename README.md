# Game: Guess the Animal
In progress...

## Problem
How can you learn a computer to ask the right questions?
The goal is to let it guess the animal you have in mind with only yes and no as options to answer and only one guess.

## Action
I've created this function with the use of a dict in Python. The computer always starts with the same question.
Each question and answer combination has a designated next question (dict in dict). The result is a 'question-tree'.
At the end there is not a next question, but an animal name, which will be the guess from the computer.
If this is wrong, the new animal and a smart question (dict) can be added.

## Result
The Python code for this game (in Dutch).

## Next steps
Create a user interface for this game, implement a tool to store the new questions and deploy the game.
