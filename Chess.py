# Chess game
import sys

class ChessGame:
    def __init__(self):
        self.board = self.make_board_list()
        self.create_board(self.board)
        self.turn = 'white'
        self.run_game()

    def create_board(self, board):
        print('   abcdefgh')
        print(' +----------+')
        for i in range(8):
            print(f'{i+1}| ', end='')
            for m in range(8):
                print(board[i][m], end='')
            print(f' |{i+1}')
        print(' +----------+')
        print('   abcdefgh')

    def make_board_list(self):
        return [['R','N','B','Q','K','B','N','R'],
                ['P','P','P','P','P','P','P','P'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['p','p','p','p','p','p','p','p'],
                ['r','n','b','q','k','b','n','r']]

    def move_piece(self, move):
        try:
            # Parse input
            num1 = move[0] + move[1]
            num2 = move[2] + move[3]
            start, end = num1, num2
            start_col, start_row = ord(start[0]) - ord('a'), int(start[1]) - 1
            end_col, end_row = ord(end[0]) - ord('a'), int(end[1]) - 1

            # Validate move (basic validation)
            if self.board[start_row][start_col] == '.':
                print("Invalid move: No piece at start position")
                return

            # Move piece
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = '.'

            # Reprint board
            self.create_board(self.board)
        except Exception as e:
            print(f"Invalid move format: {e}")

    def run_game(self):
        while True:
            print(f'It is {self.turn}\'s turn')
            user_input = input("Enter your move (e.g., e2e4 aka UCI): ")
            if user_input.lower() == 'exit':
                sys.exit()
            self.move_piece(user_input)
            self.turn = 'black' if self.turn == 'white' else 'white'

if __name__ == '__main__':
    game = ChessGame
    game.run