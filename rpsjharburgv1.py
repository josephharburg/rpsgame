#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""
import random

class Player:

    def move(self):
        return rock


    def learn(self, my_move):
        pass


    # def beats(one, two):
    #     return ((one == 'rock' and two == 'scissors') or
    #             (one == 'scissors' and two == 'paper') or
    #             (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):
    def move(self):
        randommove = random.choice(moves)
        return randommove

class HumanPlayer(Player):
    def move(self):
        humanmove = input("What is your move?:")
        invalidmove = "Im sorry thats not a valid move please try again."
        if humanmove not in moves:
            return invalidmove
        else:
            return humanmove
class MimicComputer(Player):
    def __init__(self):
        self.playerlastmove = 'rock'

    def learn(self, my_move):
        self.playerlastmove = my_move

    def move(self):
        return self.playerlastmove
class CycleComputer(Player):
    def __init__(self):
        self.computerlastmove = moves
        self.index = 0

    def move(self):
        self.index += 1
        if self.index == 3:
            self.index = 0
        return self.computerlastmove[self.index]
class Game:
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer()
        self.p2 = CycleComputer()
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1)

        if move1 == "Im sorry thats not a valid move please try again.":
            print (move1)
        while move1 == "Im sorry thats not a valid move please try again.":
            move1 = self.p1.move()
            print("Im sorry thats not a valid move please try again.")
        if move1 == 'rock':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2: #if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"The round is a Tie! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.")

            elif move2 == 'scissors':
                self.scorep1 += 1
                return print(f'Player 1 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')

            elif move2 == 'paper':
                self.scorep2 += 1
                return print(f'Player 2 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')

        if move1 == 'paper':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2: #if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"The round is a Tie! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.")

            elif move2 == 'rock':
                self.scorep1 += 1
                return print(f'Player 1 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')

            elif move2 == 'scissors':
                self.scorep2 += 1
                return  print(f'Player 2 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')

        if move1 == 'scissors':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2: #if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"The round is a Tie! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.")

            elif move2 == 'paper':
                self.scorep1 += 1
                return print(f'Player 1 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')

            elif move2 == 'rock':
                self.scorep2 += 1
                return print(f'Player 2 wins! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points.')




    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.scorep1 > self.scorep2: #If player 1 wins
            print(f"Game over! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points. Player 1 Wins!")
        if self.scorep2 > self.scorep1: #If player 2 wins
            print(f"Game over! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points. Player 2 Wins!")
        if self.scorep1 == self.scorep2: # If its a tie
            print(f"Game over! Player 1 has {self.scorep1} points. Player 2 has {self.scorep2} points. The game is a Tie!")

if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
