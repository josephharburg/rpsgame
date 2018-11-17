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


    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):
    def move(self):
        randommove = random.choice(moves)
        return randommove



class Game:
    def __init__(self, p1, p2):
        self.p1 = RandomPlayer()
        self.p2 = RandomPlayer()
        self.scorep1 = 0
        self.scorep2 = 0
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")


        if move1 == 'rock':
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


        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

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
