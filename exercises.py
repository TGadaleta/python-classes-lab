class Game():
    def __init__(self, turn='X', tie=False, winner=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
    
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
    }

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            """)
        
    def print_message(self):
        if self.tie:
            print("Tie Game!")
        elif self.winner:
            print(f"{self.winner} won the game!")
        else:
            print(f"It's {self.turn} player's turn.")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and not self.board[move]:
                self.board[move] = self.turn
                break
            print("That is not a valid move")

    def check_winner(self):
        winning_patterns = [
            ('a1', 'b1', 'c1'),
            ('a1', 'a2', 'a3'),
            ('a1', 'b2', 'c3'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            ('a3', 'b2', 'c1'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
        ]
        for box1, box2, box3 in winning_patterns:
            if self.board[box1] and self.board[box1] == self.board[box2] == self.board[box3]:
               self.winner = self.turn
    
    def check_tie(self):
        for box in self.board.values():
            if not box:
                return
        if self.winner:
            return
        self.tie = True

    def switch_turns(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Let's play some Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_tie()
            self.switch_turns()


game_instance = Game()
game_instance.play_game()
game_instance.render()

