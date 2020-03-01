# Name: Xander Houdek
# Date 02/21/20
# Description: A program to simulate the game Xiangqi, or Chinese Chess


class XiangqiGame:
    """The main class. Represents the game in multiple ways. Show board, see game state, make move, etc"""

    def __init__(self):
        """initializes the board with the game state and pieces"""

        # set game status
        self._game_state = 'UNFINISHED'  # can also be 'RED_WON' or 'BLACK_WON'
        self._turn = 'RED'               # can also be 'BLACK', alternates each turn

        # create the board
        self._board = []                     # start with blank list for board
        for i in range(10):                  # iterate 10 times
            self._board.append([])           # to make 10 y coordinates (a-i)
            for j in range(9):               # within each y coordinate, iterate 9 times
                self._board[i].append('')    # to make 9 x coordinate positions

        # initialize all red pieces
        self.Rr = Rook('red', 0, 0)
        self.Hr = Horse('red', 1, 0)
        self.Er = Elephant('red', 2, 0)
        self.Ar = Advisor('red', 3, 0)
        self.Gr = General('red', 4, 0)
        self.Ar2 = Advisor('red', 5, 0)
        self.Er2 = Elephant('red', 6, 0)
        self.Hr2 = Horse('red', 7, 0)
        self.Rr2 = Rook('red', 8, 0)
        self.Cr = Cannon('red', 1, 2)
        self.Cr2 = Cannon('red', 7, 2)
        self.Sr = Soldier('red', 0, 3)
        self.Sr2 = Soldier('red', 2, 3)
        self.Sr3 = Soldier('red', 4, 3)
        self.Sr4 = Soldier('red', 6, 3)
        self.Sr5 = Soldier('red', 8, 3)

        # initialize all black pieces
        self.Rb = Rook('black', 0, 9)
        self.Hb = Horse('black', 1, 9)
        self.Eb = Elephant('black', 2, 9)
        self.Ab = Advisor('black', 3, 9)
        self.Gb = General('black', 4, 9)
        self.Ab2 = Advisor('black', 5, 9)
        self.Eb2 = Elephant('black', 6, 9)
        self.Hb2 = Horse('black', 7, 9)
        self.Rb2 = Rook('black', 8, 9)
        self.Cb = Cannon('black', 1, 7)
        self.Cb2 = Cannon('black', 7, 7)
        self.Sb = Soldier('black', 0, 6)
        self.Sb2 = Soldier('black', 2, 6)
        self.Sb3 = Soldier('black', 4, 6)
        self.Sb4 = Soldier('black', 6, 6)
        self.Sb5 = Soldier('black', 8, 6)

        # create list of all pieces
        self._list_of_pieces = [self.Rr, self.Hr, self.Er, self.Ar, self.Gr, self.Ar2, self.Er2, self.Hr2, self.Rr2,
                                self.Cr, self.Cr2, self.Sr, self.Sr2, self.Sr3, self.Sr4, self.Sr5,
                                self.Rb, self.Hb, self.Eb, self.Ab, self.Gb, self.Ab2, self.Eb2, self.Hb2, self.Rb2,
                                self.Cb, self.Cb2, self.Sb, self.Sb2, self.Sb3, self.Sb4, self.Sb5
                                ]

        # add all pieces to board
        for piece in self._list_of_pieces:                                            # iterate through each piece
            self._board[piece.get_y_coordinate()][piece.get_x_coordinate()] = piece  # add piece to proper coordinate

    def get_piece_list(self):
        """returns private list of pieces"""
        return self._list_of_pieces

    def get_board(self):
        """returns private board attribute"""
        return self._board

    def show_board(self):
        """prints board in an easy to read manner"""
        print('  +-a--b--c--d--e--f--g--h--i--+')            # column indicators
        for row in range(len(self._board)):                  # iterates over each row, giving index
            if row == 9:                                     # on the last row,
                print(str(10) + '|-', end='')                       # change the decoration since 10 is 2 digits
            else:                                                       # on any other row,
                print(' ' + str(row + 1) + '|-', end='')                  # prints row number plus some decoration
            for column in range(len(self._board[row])):                    # iterates through each item in the row
                if self._board[row][column] != '':                         # if there is a piece in the list
                    print(self._board[row][column].get_symbol(), end='-')  # print the symbol for the piece
                else:                                                     # otherwise, if it is blank
                    print('+-', end='-')                                # prints a 'blank' space
            print('|' + str(row + 1))                               # prints row number plus some decoration
            if row in [0, 7]:                                  # if it is a specific row, will print special decoration
                print('  | |  |  |  |\ | /|  |  |  |  |')
            elif row in [1, 8]:
                print('  | |  |  |  |/ | \|  |  |  |  |')
            elif row == 9:                                   # if it is the last row
                continue                                     # skip. we don't need more decoration
            else:                                            # otherwise, if it is in any other row
                print('  | |  |  |  |  |  |  |  |  |  |')    # default decoration between each row
        print('  +-a--b--c--d--e--f--g--h--i--+')            # column indicators

    def get_game_state(self):
        """returns private game_state data member"""
        return self._game_state

    def get_turn(self):
        """returns private turn data member"""
        return self._turn

    def in_attack_range(self, x_position, y_position):
        """"returns True if the selected x and y coordinates are in attack range for any enemy piece"""
        for piece in self._list_of_pieces:  # iterate through all pieces
            if piece != self._board[y_position][x_position]:  # ignores selected piece
                if piece.get_symbol()[-1] != self.get_turn()[0].lower():  # if piece in list is opposite color
                    if piece.is_legal_move(self, x_position, y_position):  # if enemy piece can move to piece's pos
                        return True
        return False

    def is_in_check(self, color):
        """checks if player is in check, returns True if they are in check and returns False otherwise"""
        if color == 'red' and self.in_attack_range(self.Gr.get_x_coordinate(), self.Gr.get_y_coordinate()):
            return True
        if color == 'black' and self.in_attack_range(self.Gb.get_x_coordinate(), self.Gb.get_y_coordinate()):
            return True
        return False

    def check_move_rules(self, selected_piece, end_x, end_y):
        """check rules that apply to all pieces, and calls piece-specific rule check"""
        if self._game_state != 'UNFINISHED':  # if the game has ended
            return False
        if not selected_piece:  # if we did not find a piece at the starting coordinates
            return False
        if selected_piece.get_x_coordinate() == end_x and selected_piece.get_y_coordinate() == end_y:
            return False
        if end_x > 8 or end_x < 0 or end_y > 9 or end_y < 0:  # if the proposed move is out of bounds
            return False
        # if the space that the piece is trying to move to is occupied by a piece of the same color
        if self._board[end_y][end_x] != '':
            if self._board[end_y][end_x].get_color() == selected_piece.get_color():
                return False
        if not selected_piece.is_legal_move(self, end_x, end_y):  # if the desired move is illegal on a per piece basis
            return False
        # temporarily make move to ensure the current player is not in check
        self._board[int(selected_piece.get_y_coordinate())][int(selected_piece.get_x_coordinate())] = ''
        temp = self._board[end_y][end_x]  # save this piece so nothing gets permanently captured
        self._board[end_y][end_x] = selected_piece
        if self.is_in_check(self._turn.lower()):  # if the move puts or leaves the general in check
            # return pieces to original place
            self._board[int(selected_piece.get_y_coordinate())][int(selected_piece.get_x_coordinate())] = selected_piece
            self._board[end_y][end_x] = temp
            return False

        # return pieces to original place
        self._board[int(selected_piece.get_y_coordinate())][int(selected_piece.get_x_coordinate())] = selected_piece
        self._board[end_y][end_x] = temp
        return True

    def make_move(self, start, end):
        """
        if move is legal, moves piece from start position to end position, captures enemy if applicable,
        changes whose turn it is, and returns True. otherwise, returns False
        """
        start_xy = alphanumerical_to_xy(start)  # convert start coordinates to x and y coordinates
        start_x = start_xy[0]                   # isolate x coordinate
        start_y = start_xy[1]                   # isolate y coordinate
        end_xy = alphanumerical_to_xy(end)      # convert end coordinates to x and y coordinates
        end_x = end_xy[0]                       # isolate x coordinate
        end_y = end_xy[1]                       # isolate y coordinate

        # find the desired piece in list
        selected_piece = self._board[start_y][start_x]

        # if the color of the starting piece does not match the color of whose turn it is
        if selected_piece.get_symbol()[1] != self.get_turn()[0].lower():
            return False

        if not self.check_move_rules(selected_piece, end_x, end_y):  # if the selected move is illegal
            return False

        # make moves
        if self._board[end_y][end_x] != '':         # if the new location is occupied by an enemy
            self._list_of_pieces.remove(self._board[end_y][end_x])  # remove the enemy object from the list of pieces
        self._board[end_y][end_x] = selected_piece  # move piece to new location, replacing captured piece if applicable
        self._board[start_y][start_x] = ''          # make old location blank
        selected_piece.set_position(end_x, end_y)   # change position on piece

        self.check_victory()  # checks to see if game has been won, and adjusts game state accordingly

        # change whose turn it is
        if self._turn == "RED":
            self._turn = "BLACK"
        elif self._turn == "BLACK":
            self._turn = "RED"

        return True

    def check_victory(self):
        """returns True if a victory condition is met, otherwise returns False. Covers checkmate and stalemate"""
        any_legal_moves = False  # default value, assume there are no legal moves for the opposing player to make
        for piece in self._list_of_pieces:  # iterates through all pieces
            print(piece.get_symbol(), ':')
            for x_coordinate in range(9):   # iterates through each coordinate on the board
                for y_coordinate in range(10):
                    if piece.get_symbol()[1] != self._turn[0].lower():  # if piece is owned by "defending" player
                        if self.check_move_rules(piece, x_coordinate, y_coordinate):  # if move is legal
                            print(x_coordinate, y_coordinate)
                            any_legal_moves = True  # then there is at least one move where player can get out of check

        if not any_legal_moves:
            self._game_state = self._turn + '_WON'  # the player who just made a move won


class Piece:
    """A class to represent a game piece"""

    def __init__(self, color, x_position, y_position):
        """initializes the object representing the piece"""
        self._color = color            # can be red or black
        self._x_position = x_position  # start with original position
        self._y_position = y_position  # start with original position
        self._symbol = None            # placeholder, gets filled in for each inherited class

    def get_color(self):
        """returns private color attribute"""
        return self._color

    def get_x_coordinate(self):
        """returns the private x position attribute"""
        return self._x_position

    def get_y_coordinate(self):
        """returns the private y position attribute"""
        return self._y_position

    def set_position(self, new_x_position, new_y_position):
        """sets private position attributes to parameter"""
        self._x_position = new_x_position
        self._y_position = new_y_position

    def get_symbol(self):
        """returns private symbol attribute"""
        return self._symbol


class General(Piece):
    """A class to represent the general piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'G' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # general can only ever move one space
        if end_x - self._x_position not in [-1, 0, 1] or end_y - self._y_position not in [-1, 0, 1]:
            return False

        # general cannot move diagonally, so one position difference must be 0
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position in [-1, 1]:
            return False

        # general cannot place itself in the attack lines of any enemy piece
        in_attack_lines = False
        for piece in board.get_piece_list():  # iterate through all pieces
            if piece.get_symbol()[-1] != self._color[0]:  # if piece in list is opposite color
                if piece.is_legal_move(board, end_x, end_y):  # if enemy piece can move to piece's pos
                    in_attack_lines = True
        if in_attack_lines:
            return False

        # general cannot move to a position where it is directly facing enemy general with no pieces in between
        enemy_general = None  # default value
        for piece in board.get_piece_list():     # iterate over every piece in list
            # if the symbol matches the symbol of the enemy general
            if piece.get_symbol()[0] == 'G' and piece.get_symbol()[1] != board.get_turn()[0].lower():
                enemy_general = piece                  # assign piece to variable
        if end_x == enemy_general.get_x_coordinate():  # if the desired x coordinate is the same as the enemy general's
            blocking_pieces = False                    # default value, assume there are no pieces in the way
            for y_coordinate in range(10):             # iterates over each y coordinate, giving index
                if board.get_board()[y_coordinate][end_x] != '':  # if there is any piece along the x_coordinate
                    blocking_pieces = True             # reassign variable to reflect that
            if not blocking_pieces:                    # if there are no pieces in the way
                return False                           # would activate the 'flying general' move, and is thus illegal

        return True


class Advisor(Piece):
    """A class to represent the advisor piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'A' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False."""
        # advisor can only ever move one space diagonally
        if end_x - self._x_position not in [-1, 1] or end_y - self._y_position not in [-1, 1]:
            return False

        # advisor can not leave the palace
        if end_x not in [3, 4, 5] or end_y not in [0, 1, 2, 7, 8, 9]:
            return False

        return True


class Elephant(Piece):
    """A class to represent the elephant piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'E' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # elephant moves diagonally 2 spaces at a time
        if end_x - self._x_position not in [-2, 2] or end_y - self._y_position not in [-2, 2]:
            return False

        # elephant may not jump over intervening pieces
        if end_x - self._x_position == -2 and end_y - self._y_position == -2:
            if board.get_board()[self._y_position - 1][self._x_position - 1] != '':
                return False
        if end_x - self._x_position == -2 and end_y - self._y_position == 2:
            if board.get_board()[self._y_position + 1][self._x_position - 1] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position == 2:
            if board.get_board()[self._y_position + 1][self._x_position + 1] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position == -2:
            if board.get_board()[self._y_position - 1][self._x_position + 1] != '':
                return False

        # elephant may not cross river
        if self._symbol[1] == 'r' and end_y not in [0, 1, 2, 3, 4]:
            return False
        if self._symbol[1] == 'b' and end_y not in [5, 6, 7, 8, 9]:
            return False

        return True


class Horse(Piece):
    """A class to represent the horse piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'H' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # horse moves one space orthogonally and one space diagonally away from the orthogonal move
        if end_x - self._x_position not in [-2, -1, 1, 2] or end_y - self._y_position not in [-2, -1, 1, 2]:
            return False
        if end_x - self._x_position in [-2, 2] and end_y - self._y_position not in [-1, 1]:
            return False
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position not in [-2, 2]:
            return False

        # horses may not jump over intervening pieces (on the orthogonal move):
        if end_x - self._x_position == -2 and end_y - self._y_position in [-1, 1]:
            if board.get_board()[self._y_position][self._x_position - 1] != '':
                return False
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position == -2:
            if board.get_board()[self._y_position - 1][self._x_position] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position in [-1, 1]:
            if board.get_board()[self._y_position][self._x_position + 1] != '':
                return False
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position == 2:
            if board.get_board()[self._y_position + 1][self._x_position] != '':
                return False

        return True


class Rook(Piece):
    """A class to represent the rook piece (aka the chariot). Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'R' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # rooks move orthogonally in any direction
        if end_x - self._x_position != 0 and end_y - self._y_position != 0:
            return False

        # rooks cannot jump over intervening pieces
        if end_x - self._x_position > 0:    # if the rook moves right
            for x_position in range(self._x_position + 1, end_x):  # iterate over all indexes between start and end
                if board.get_board()[self._y_position][x_position] != '':
                    return False
        if end_x - self._x_position < 0:    # if the rook moves left
            for x_position in range(end_x + 1, self._x_position):  # iterate over all indexes between end and start
                if board.get_board()[self._y_position][x_position] != '':
                    return False
        if end_y - self._y_position > 0:    # if the rook moves down
            for y_position in range(self._y_position + 1, end_y):  # iterate over all indexes between start and end
                if board.get_board()[y_position][self._x_position] != '':
                    return False
        if end_y - self._y_position < 0:  # if the rook moves up
            for y_position in range(end_y + 1, self._y_position):  # iterate over all indexes between end and start
                if board.get_board()[y_position][self._x_position] != '':
                    return False

        return True


class Cannon(Piece):
    """A class to represent the cannon piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'C' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # cannons move similar to rooks, orthogonally in any direction
        if end_x - self._x_position != 0 and end_y - self._y_position != 0:
            return False

        # if the proposed move is to an empty space (ie, when not capturing), the rules are the same as rook
        if board.get_board()[end_y][end_x] == '':
            if end_x - self._x_position > 0:    # if the rook moves right
                for x_position in range(self._x_position + 1, end_x):  # iterate over all indexes between start and end
                    if board.get_board()[self._y_position][x_position] != '':
                        return False
            if end_x - self._x_position < 0:    # if the rook moves left
                for x_position in range(end_x + 1, self._x_position):  # iterate over all indexes between end and start
                    if board.get_board()[self._y_position][x_position] != '':
                        return False
            if end_y - self._y_position > 0:    # if the rook moves down
                for y_position in range(self._y_position + 1, end_y):  # iterate over all indexes between start and end
                    if board.get_board()[y_position][self._x_position] != '':
                        return False
            if end_y - self._y_position < 0:  # if the rook moves up
                for y_position in range(end_y + 1, self._y_position):  # iterate over all indexes between end and start
                    if board.get_board()[y_position][self._x_position] != '':
                        return False

        # however, when capturing a piece, the rook must have exactly 1 piece in between it and its target
        else:   # note that we have already ensured that the target is either empty or contains an enemy in make_move
            screen = []  # screen is a common name for the piece that allows the cannon to capture
            if end_x - self._x_position > 0:    # if the rook moves right
                for x_position in range(self._x_position + 1, end_x):  # iterate over all indexes between start and end
                    if board.get_board()[self._y_position][x_position] != '':
                        screen.append(board.get_board()[self._y_position][x_position])  # add piece to list of screens
            if end_x - self._x_position < 0:    # if the rook moves left
                for x_position in range(end_x + 1, self._x_position):  # iterate over all indexes between end and start
                    if board.get_board()[self._y_position][x_position] != '':
                        screen.append(board.get_board()[self._y_position][x_position])  # add piece to list of screens
            if end_y - self._y_position > 0:    # if the rook moves down
                for y_position in range(self._y_position + 1, end_y):  # iterate over all indexes between start and end
                    if board.get_board()[y_position][self._x_position] != '':
                        screen.append(board.get_board()[y_position][self._x_position])  # add piece to list of screens
            if end_y - self._y_position < 0:  # if the rook moves up
                for y_position in range(end_y + 1, self._y_position):  # iterate over all indexes between end and start
                    if board.get_board()[y_position][self._x_position] != '':
                        screen.append(board.get_board()[y_position][self._x_position])  # add piece to list of screens

            if len(screen) != 1:    # the list must contain exactly one element
                return False

        return True


class Soldier(Piece):
    """A class to represent the soldier piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'S' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """returns True if proposed move is legal, otherwise returns False"""
        # before the river, soldiers may only move forward one space
        if self._symbol[1] == 'r' and self._y_position in [3, 4] and end_y - self._y_position != 1:
            return False
        if self._symbol[1] == 'b' and self._y_position in [5, 6] and end_y - self._y_position != -1:
            return False
        if self._symbol[1] == 'r' and self._y_position in [3, 4] and self._x_position - end_x != 0:
            return False
        if self._symbol[1] == 'b' and self._y_position in [5, 6] and self._x_position - end_x != 0:
            return False

        # after the river, soldier may also move sideways
        if self._symbol[1] == 'r' and self._y_position in [5, 6, 7, 8, 9]:
            if end_y - self._y_position == 1 and end_x - self._x_position != 0:
                return False
            if end_y - self._y_position == 0 and end_x - self._x_position not in [-1, 1]:
                return False
        if self._symbol[1] == 'b' and self._x_position in [0, 1, 2, 3, 4]:
            if end_y - self._y_position == -1 and end_x - self._x_position != 0:
                return False
            if end_y - self._y_position == 0 and end_x - self._x_position not in [-1, 1]:
                return False

        # soldiers may never retreat
        if self._symbol[1] == 'r' and end_y - self._y_position < 0:
            return False
        if self._symbol[1] == 'b' and end_y - self._y_position > 0:
            return False

        return True


# static function
def alphanumerical_to_xy(alphanumerical):
    """converts alphanumerical position to a tuple with x/y coordinates"""
    # default values
    x_position = None
    y_position = None

    # determine x position based off of letter
    if alphanumerical[0] == 'a':
        x_position = 0
    elif alphanumerical[0] == 'b':
        x_position = 1
    elif alphanumerical[0] == 'c':
        x_position = 2
    elif alphanumerical[0] == 'd':
        x_position = 3
    elif alphanumerical[0] == 'e':
        x_position = 4
    elif alphanumerical[0] == 'f':
        x_position = 5
    elif alphanumerical[0] == 'g':
        x_position = 6
    elif alphanumerical[0] == 'h':
        x_position = 7
    elif alphanumerical[0] == 'i':
        x_position = 8

    # determine y position based off of number
    if len(alphanumerical) == 2:
        y_position = int(alphanumerical[1]) - 1
    elif len(alphanumerical) == 3:
        y_position = int(alphanumerical[1] + alphanumerical[2]) - 1
    return x_position, y_position


def main():
    """used for testing"""
    # game = XiangqiGame()
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # print(game.make_move('e1', 'e2'))
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # print(game.make_move('c7', 'c6'))
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # print(game.make_move('b3', 'c3'))
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # print(game.make_move('b10', 'c8'))
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # print(game.make_move('c3', 'c6'))
    # game.show_board()
    #
    # print(game.get_game_state())
    # print(game.get_turn())
    # game.show_board()




    game = XiangqiGame()
    game.make_move('b3', 'e3')
    game.make_move('h8', 'e8')
    game.make_move('h3', 'h6')
    game.make_move('b8', 'b4')
    game.make_move('e3', 'e7')  # black is in check
    game.make_move('e8', 'e4')
    print(game.make_move('h6', 'e6'))  # black is mated here according to wikipedia
    game.show_board()
    print(game.get_game_state())
    print(game.get_turn())
    print('black in check:', game.is_in_check('black'))

    for piece in game._list_of_pieces:
        print(piece.get_symbol() + ':')
        for x in range(9):
            for y in range(10):
                if game.check_move_rules(piece, x, y):
                    print(x, y)




    # game = XiangqiGame()
    # game.show_board()
    # for piece in game._list_of_pieces:
    #     print(piece.get_symbol() + ':')
    #     for x in range(9):
    #         for y in range(10):
    #             if game.check_move_rules(piece, x, y):
    #                 print(x, y)


if __name__ == '__main__':
    main()
