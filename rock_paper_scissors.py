#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################################################################
# rock paper scissors - (c) 2021 CHAITANYA GOTHWAL - MIT License - Use at your own risk, no warranty!
########################################################################################################################

# STANDARD IMPORTS
import random
from typing import Union


def main_game() -> None:
    computers_choice: str = random.SystemRandom().choice('rps')
    user_choice: str = input('Your turn: Rock Paper Scissor [r/p/s]').lower()

    if user_choice not in 'rps' or user_choice == '':
        raise ValueError('invalid option')

    def the_computer_won() -> bool:
        """ since the computer is a computer, it will lose in a tie """
        if user_choice == computers_choice:
            return False  # the computer loses in a tie

        if user_choice == 'r' and computers_choice == 'p':
            return True

        if user_choice == 'p' and computers_choice == 's':
            return True

        if user_choice == 's' and computers_choice == 'r':
            return True

        return False

    if the_computer_won():
        print(f'Oh no! The computer won with: {computers_choice}.')
    else:
        print(f'Nice! You won with {user_choice} against the computer: {computers_choice}.')


if __name__ == '__main__':
    print("NOTE: you will winn if it's a tie")
    done: bool = False
    while not done:
        main_game()
        if input('do you want to play again [Y/n]').lower() == 'n':
            done = True
