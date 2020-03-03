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

        # initialize all red pieces where first letter is piece name and second letter is color
        self._rr = Rook('red', 0, 0)
        self._hr = Horse('red', 1, 0)
        self._er = Elephant('red', 2, 0)
        self._ar = Advisor('red', 3, 0)
        self._gr = General('red', 4, 0)
        self._ar2 = Advisor('red', 5, 0)
        self._er2 = Elephant('red', 6, 0)
        self._hr2 = Horse('red', 7, 0)
        self._rr2 = Rook('red', 8, 0)
        self._cr = Cannon('red', 1, 2)
        self._cr2 = Cannon('red', 7, 2)
        self._sr = Soldier('red', 0, 3)
        self._sr2 = Soldier('red', 2, 3)
        self._sr3 = Soldier('red', 4, 3)
        self._sr4 = Soldier('red', 6, 3)
        self._sr5 = Soldier('red', 8, 3)

        # initialize all black pieces where first letter is piece name and second letter is color
        self._rb = Rook('black', 0, 9)
        self._hb = Horse('black', 1, 9)
        self._eb = Elephant('black', 2, 9)
        self._ab = Advisor('black', 3, 9)
        self._gb = General('black', 4, 9)
        self._ab2 = Advisor('black', 5, 9)
        self._eb2 = Elephant('black', 6, 9)
        self._hb2 = Horse('black', 7, 9)
        self._rb2 = Rook('black', 8, 9)
        self._cb = Cannon('black', 1, 7)
        self._cb2 = Cannon('black', 7, 7)
        self._sb = Soldier('black', 0, 6)
        self._sb2 = Soldier('black', 2, 6)
        self._sb3 = Soldier('black', 4, 6)
        self._sb4 = Soldier('black', 6, 6)
        self._sb5 = Soldier('black', 8, 6)

        # create list of all pieces
        self._list_of_pieces = [self._rr, self._hr, self._er, self._ar, self._gr, self._ar2, self._er2, self._hr2,
                                self._rr2, self._cr, self._cr2, self._sr, self._sr2, self._sr3, self._sr4, self._sr5,
                                self._rb, self._hb, self._eb, self._ab, self._gb, self._ab2, self._eb2, self._hb2,
                                self._rb2, self._cb, self._cb2, self._sb, self._sb2, self._sb3, self._sb4, self._sb5
                                ]

        # add all pieces to board
        for piece in self._list_of_pieces:                                            # iterate through each piece
            self._board[piece.get_y_coordinate()][piece.get_x_coordinate()] = piece   # add piece to proper coordinate

    # get methods
    def get_piece_list(self):
        """returns private list of pieces"""
        return self._list_of_pieces

    def get_board(self):
        """returns private board attribute"""
        return self._board

    def get_game_state(self):
        """returns private game_state data member"""
        return self._game_state

    def get_turn(self):
        """returns private turn data member"""
        return self._turn

    def show_board(self):
        """prints board in an easy to read manner"""
        print('    a  b  c  d  e  f  g  h  i   ')            # column indicators
        print('  +----------------------------+')
        for row in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:                  # iterates over each row, giving index
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
            if row in [2, 9]:                                  # if it is a specific row, will print special decoration
                print('  | |  |  |  |\ | /|  |  |  |  |')
            elif row in [1, 8]:
                print('  | |  |  |  |/ | \|  |  |  |  |')
            elif row == 0:                                   # if it is the last row
                continue                                     # skip. we don't need more decoration
            elif row == 5:                                   # if it is the middle
                print('  |                            |')    # print the river
            else:                                            # otherwise, if it is in any other row
                print('  | |  |  |  |  |  |  |  |  |  |')    # default decoration between each row
        print('  +----------------------------+')
        print('    a  b  c  d  e  f  g  h  i   ')            # column indicators

    def in_attack_range(self, x_position, y_position):
        """"returns True if the selected x and y coordinates are in attack range for any enemy piece"""
        for piece in self._list_of_pieces:                                    # iterate through all pieces
            if piece != self._board[y_position][x_position]:                  # ignores selected piece
                if piece.get_symbol()[-1] != self.get_turn()[0].lower():      # if piece in list is opposite color
                    if self.check_move_rules(piece, x_position, y_position):  # if enemy piece can move to position
                        return True                                           # then the position is in attack range
        return False                                                          # if not, position is not in attack range

    def is_in_check(self, color):
        """checks if player is in check, returns True if they are in check and returns False otherwise"""
        # checks which color is selected, then checks if the corresponding general's position is in attack range
        if color == 'red' and self.in_attack_range(self._gr.get_x_coordinate(), self._gr.get_y_coordinate()):
            return True
        if color == 'black' and self.in_attack_range(self._gb.get_x_coordinate(), self._gb.get_y_coordinate()):
            return True
        return False  # if either not the color or the general is not in attack range

    def check_move_rules(self, selected_piece, end_x, end_y):
        """check rules that apply to all pieces, and calls piece-specific rule check"""
        # if move is to the same position that it is currently in
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

        # temporarily make move
        self._board[int(selected_piece.get_y_coordinate())][int(selected_piece.get_x_coordinate())] = ''
        temp = self._board[end_y][end_x]  # save this piece so nothing gets permanently captured
        self._board[end_y][end_x] = selected_piece

        # cannot leave the general in the attack lines of any enemy piece
        general = None  # default value, will be changed to general of the same color
        enemy_general = None  # default value
        if selected_piece.get_symbol()[1] == 'r':
            general = self._gr
            enemy_general = self._gb
        elif selected_piece.get_symbol()[1] == 'b':
            general = self._gb
            enemy_general = self._gr

        in_attack_lines = False  # default value
        # if the piece is not currently attacking the enemy general (bc then it doesn't matter if general is in danger)
        if end_x != enemy_general.get_x_coordinate() or end_y != enemy_general.get_y_coordinate():
            for piece in self._list_of_pieces:                              # iterate through all pieces
                if piece.get_symbol()[1] != selected_piece.get_color()[0]:  # if piece in list is opposite color
                    if piece.is_legal_move(self, general.get_x_coordinate(), general.get_y_coordinate()):
                        # if the enemy piece can legally make a move to the general position
                        in_attack_lines = True                              # change value to reflect that

        # also cannot maneuver in a way where generals face each other without any pieces separating them
        flying_general = False
        if self._gb.get_x_coordinate() == self._gr.get_x_coordinate():  # if they are on the same y coordinate
            flying_general = True
            for y_coordinate in range(self._gr.get_y_coordinate() + 1, self._gb.get_y_coordinate()):
                if self._board[y_coordinate][self._gb.get_x_coordinate()] != '':  # if the space is occupied by a piece
                    flying_general = False  # then flying general does not apply

        # reset pieces to original position, regardless of if the move is legal or not
        self._board[int(selected_piece.get_y_coordinate())][int(selected_piece.get_x_coordinate())] = selected_piece
        self._board[end_y][end_x] = temp
        if in_attack_lines:  # if the move puts or leaves the general in the attack lines
            return False
        if flying_general:
            return False

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
        if selected_piece == '':  # if the start position does not contain a piece
            return False

        # if the color of the starting piece does not match the color of whose turn it is
        if selected_piece.get_symbol()[1] != self.get_turn()[0].lower():
            return False

        if self._game_state != 'UNFINISHED':  # if the game has ended
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
            for x_coordinate in range(9):   # iterates through each coordinate on the board
                for y_coordinate in range(10):
                    if piece.get_symbol()[1] != self._turn[0].lower():  # if piece is owned by "defending" player
                        if self.check_move_rules(piece, x_coordinate, y_coordinate):  # if move is legal
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
        in_attack_lines = False                               # default value
        for piece in board.get_piece_list():                  # iterate through all pieces
            if piece.get_symbol()[-1] != self._color[0]:      # if piece in list is opposite color
                if piece.is_legal_move(board, end_x, end_y):  # if enemy piece can move to piece's pos
                    in_attack_lines = True
        if in_attack_lines:
            return False

        return True


class Advisor(Piece):
    """A class to represent the advisor piece. Inherited from the Piece class"""
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)  # inherits from the piece class
        self._symbol = 'A' + self._color[0]       # make symbol first letter of class and first letter of color

    def is_legal_move(self, board, end_x, end_y):
        """
        returns True if proposed move is legal, otherwise returns False. Note that board parameter is not used here but
        is used in other Piece classes, and is left in to allow all pieces to be looped over.
        """
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
        if end_x - self._x_position == -2 and end_y - self._y_position == -2:  # if the piece moves up and left
            if board.get_board()[self._y_position - 1][self._x_position - 1] != '':
                return False
        if end_x - self._x_position == -2 and end_y - self._y_position == 2:   # if the piece moves down and left
            if board.get_board()[self._y_position + 1][self._x_position - 1] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position == 2:    # if the piece moves down and right
            if board.get_board()[self._y_position + 1][self._x_position + 1] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position == -2:   # if the piece moves up and right
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
        if end_x - self._x_position == -2 and end_y - self._y_position in [-1, 1]:  # if the piece moves left first
            if board.get_board()[self._y_position][self._x_position - 1] != '':
                return False
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position == -2:  # if the piece moves up first
            if board.get_board()[self._y_position - 1][self._x_position] != '':
                return False
        if end_x - self._x_position == 2 and end_y - self._y_position in [-1, 1]:  # if the piece moves right first
            if board.get_board()[self._y_position][self._x_position + 1] != '':
                return False
        if end_x - self._x_position in [-1, 1] and end_y - self._y_position == 2:  # if the piece moves down first
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
            if end_x - self._x_position > 0:    # if the cannon moves right
                for x_position in range(self._x_position + 1, end_x):  # iterate over all indexes between start and end
                    if board.get_board()[self._y_position][x_position] != '':
                        return False
            if end_x - self._x_position < 0:    # if the cannon moves left
                for x_position in range(end_x + 1, self._x_position):  # iterate over all indexes between end and start
                    if board.get_board()[self._y_position][x_position] != '':
                        return False
            if end_y - self._y_position > 0:    # if the cannon moves down
                for y_position in range(self._y_position + 1, end_y):  # iterate over all indexes between start and end
                    if board.get_board()[y_position][self._x_position] != '':
                        return False
            if end_y - self._y_position < 0:  # if the cannon moves up
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
        """
        returns True if proposed move is legal, otherwise returns False. Note that board parameter is not used here but
        is used in other Piece classes, and is left in to allow all pieces to be looped over.
        """
        # before the river, soldiers may only move forward one space
        if self._symbol[1] == 'r' and self._y_position in [3, 4] and end_y - self._y_position != 1:
            return False
        if self._symbol[1] == 'r' and self._y_position in [3, 4] and self._x_position - end_x != 0:
            return False
        if self._symbol[1] == 'b' and self._y_position in [5, 6] and end_y - self._y_position != -1:
            return False
        if self._symbol[1] == 'b' and self._y_position in [5, 6] and self._x_position - end_x != 0:
            return False

        # after the river, soldier may also move sideways
        if self._symbol[1] == 'r' and self._y_position in [5, 6, 7, 8, 9]:  # if the piece is past the river
            if end_y - self._y_position not in [0, 1] or end_x - self._x_position not in [-1, 0, 1]:
                return False
            if end_y - self._y_position == 1 and end_x - self._x_position != 0:  # if piece moves forward and to side
                return False
            if end_y - self._y_position == 0 and end_x - self._x_position not in [-1, 1]:  # if piece moves >1 space
                return False
        if self._symbol[1] == 'b' and self._x_position in [0, 1, 2, 3, 4]:  # if the piece is past the river
            if end_y - self._y_position not in [0, -1] or end_x - self._x_position not in [-1, 0, 1]:
                return False
            if end_y - self._y_position == -1 and end_x - self._x_position != 0:  # if piece moves forward and to side
                return False
            if end_y - self._y_position == 0 and end_x - self._x_position not in [-1, 1]:  # if piece moves >1 space
                return False

        # soldiers may never retreat
        if self._symbol[1] == 'r' and end_y - self._y_position < 0:
            return False
        if self._symbol[1] == 'b' and end_y - self._y_position > 0:
            return False

        return True


# static function because it is not attached to any class
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
        y_position = int(alphanumerical[1]) - 1  # converts to int and subtracts 1 (because lists start at 0)
    elif len(alphanumerical) == 3:  # this block is to allow for 10 on y axis, e.g. 'f10'
        y_position = int(alphanumerical[1] + alphanumerical[2]) - 1  # converts to int and subtracts 1
    return x_position, y_position  # returns a tuple to be manipulated in make_move


def main():
    """used for testing. Think of this as scratch paper. See Xiangqi_unit_tests.py for actual tests"""
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
    #
    # game = XiangqiGame()
    # print(game.make_move('b3', 'e3'))
    # print(game.get_turn())
    # print(game.get_game_state())
    # print(game.make_move('h8', 'e8'))
    # print(game.make_move('h3', 'h6'))
    # print(game.make_move('b8', 'b4'))
    # print('black in check:', game.is_in_check('black'))  # should be False
    # print(game.get_game_state())
    # print(game.make_move('e3', 'e7'))  # black in check
    # print(game.get_game_state())
    # game.show_board()
    # # print('black in check:', game.is_in_check('black'))
    # # print(game.get_game_state())
    # # print(game.make_move('e8', 'e4'))
    # # print(game.make_move('h6', 'e6'))  # black is checkmated here according to wikipedia
    # # game.show_board()
    # # print(game.get_game_state())
    # # print(game.get_turn())
    # print('black in check:', game.is_in_check('black'))
    # print('red in check:', game.is_in_check('red'))

    game = XiangqiGame()
    game.make_move('c4', 'c5')
    game.make_move('a7', 'a6')
    game.make_move('c5', 'c6')  # wins game for some reason
    game.show_board()

    for piece in game.get_piece_list():
        print(piece.get_symbol() + ':')
        for x in range(9):
            for y in range(10):
                if game.check_move_rules(piece, x, y):
                    print(x, y)


if __name__ == '__main__':
    main()
