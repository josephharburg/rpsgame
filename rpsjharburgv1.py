#!/usr/bin/env python3
import random
moves = ['rock', 'paper', 'scissors']


class Player:
    def printerror(self, color):
        print("\033[91m {}\033[00m" .format(color))

    def move(self):
        return rock

    def learn(self, my_move):
        pass

    def Numberofrounds(self):
        isint = False
        while isint is False:
            self.whatnumber = input("How Many rounds do you want to play?:")
            try:
                self.rounds = int(self.whatnumber)
                isint = True
                return self.rounds
            except ValueError:
                self.printerror("Im sorry that is not a number!")


class RandomPlayer(Player):
    def move(self):
        randommove = random.choice(moves)
        return randommove


class HumanPlayer(Player):

    def move(self):
        validmove = False
        while validmove is False:
            humanmove = input("What is your move?:").lower()
            if humanmove in moves:
                validmove = True
                return humanmove
            else:
                self.printerror("Thats not a valid move please try again.")


class MimicComputer(Player):
    def __init__(self):
        self.playerlastmove = 'rock'

    def learn(self, my_move):
        self.playerlastmove = my_move

    def move(self):
        return self.playerlastmove


class Cycle(Player):
    def __init__(self):
        self.computerlastmove = moves
        self.index = 0

    def move(self):
        if self.index <= 1:
            self.index += 1
            return self.computerlastmove[self.index]
        else:
            self.index = 0
            return self.computerlastmove[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer()
        self.p2 = random.choice([RandomPlayer(), MimicComputer(), Cycle()])
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        Tie = "This round is a Tie!"
        p1wins = 'Player 1 wins!'
        p2wins = 'Player 2 wins!'
        s1 = '\nScore:\nPlayer 1:'
        s2 = '\nPlayer 2:'
        self.p2.learn(move1)
        self.p1.learn(move2)
        if move1 == 'rock':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2:     # if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"{Tie} {s1}{self.scorep1} {s2}{self.scorep2}")

            elif move2 == 'scissors':
                self.scorep1 += 1
                return print(f'{p1wins} {s1}{self.scorep1} {s2}{self.scorep2}')

            elif move2 == 'paper':
                self.scorep2 += 1
                return print(f'{p2wins} {s1}{self.scorep1} {s2}{self.scorep2}')

        if move1 == 'paper':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2:     # if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"{Tie} {s1}{self.scorep1} {s2}{self.scorep2}")

            elif move2 == 'rock':
                self.scorep1 += 1
                return print(f'{p1wins} {s1}{self.scorep1} {s2}{self.scorep2}')

            elif move2 == 'scissors':
                self.scorep2 += 1
                return print(f'{p2wins} {s1}{self.scorep1} {s2}{self.scorep2}')

        if move1 == 'scissors':
            print(f"Player 1: {move1}  Player 2: {move2}")
            if move1 == move2:     # if the moves are the same
                self.scorep1 += 1
                self.scorep2 += 1
                return print(f"{Tie} {s1}{self.scorep1} {s2}{self.scorep2}")

            elif move2 == 'paper':
                self.scorep1 += 1
                return print(f'{p1wins} {s1}{self.scorep1} {s2}{self.scorep2}')

            elif move2 == 'rock':
                self.scorep2 += 1
                return print(f'{p2wins} {s1}{self.scorep1} {s2}{self.scorep2}')

    def play_game(self):
        print("Game start!")
        for round in range(self.p1.Numberofrounds()):
            print(f"Round {round}:")
            self.play_round()
        if self.scorep1 > self.scorep2:   # If player 1 wins
            print('\33[94m' + 'Game over! Player 1 Wins!' + '\033[0m')
        if self.scorep2 > self.scorep1:   # If player 2 wins
            print('\33[94m' + 'Game over! Player 2 Wins!' + '\033[0m')
        if self.scorep1 == self.scorep2:   # If its a tie
            print('\33[94m' + 'Game over! The game is a Tie!' + '\033[0m')


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
