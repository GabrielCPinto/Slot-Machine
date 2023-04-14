import random
from .constants import MAX_LINES, MAX_BET, MIN_BET, COLS


class Slot_machine:

    symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
    }
    symbol_values = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }

    def __init__(self):
        pass

    def deposit(self):
        while True:
            self.amount = input('Deposit: ')
            if self.amount.isdigit():
                self.amount = int(self.amount)
                if self.amount > 0:
                    break
                else:
                    print('Invalid deposit')
            else:
                print('Invalid deposit')

    def get_bet(self):
        while True:
            self.bet = input('bet: ')
            if self.bet.isdigit():
                self.bet = int(self.bet)
                if self.amount >= self.bet:
                    if MIN_BET <= self.bet <= MAX_BET:
                        self.amount -= self.bet * self.lines
                        break
                    else:
                        print('Invalid bet')
                else:
                    print('Invalid bet')
            else:
                print('Invalid bet')

    def get_lines(self):
        while True:
            self.lines = input(
                f'Enter the number of lines to bet on (1 - {MAX_LINES})?: ')
            if self.lines.isdigit():
                self.lines = int(self.lines)
                if 0 < self.lines <= MAX_LINES:
                    break
                else:
                    print('Invalid lines')
            else:
                print('Invalid lines')

    def get_spin(self, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        self.col = []
        for _ in range(COLS):
            col = []
            current_symbols = all_symbols[:]
            for _ in range(MAX_LINES):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                col.append(value)
            self.col.append(col)

    def get_cols(self):
        for row in range(len(self.col[0])):
            for i, col in enumerate(self.col):
                if i != len(col) - 1:
                    print(col[row], end=' | ')
                else:
                    print(col[row])

    def check_winnings(self, values):
        winnings = 0
        for line in range(self.lines):
            symbol = self.col[0][line]
            for col in self.col:
                symbol_check = col[line]
                if symbol != symbol_check:
                    break
            else:
                winnings += values[symbol] * self.bet
        self.amount += winnings
        print(f'winnings: {winnings}')

    def run(self):
        self.deposit()
        run = 'Y'
        while run == 'Y':
            self.get_lines()
            self.get_bet()
            print(
                f'you are betting ${self.bet} on {self.lines}. Total bet: {self.bet*self.lines}')
            self.get_spin(self.symbol_count)
            self.get_cols()
            self.check_winnings(self.symbol_values)
            print(f'Total: {self.amount}')
            run = input('Continue?(Y/N) ').upper()
