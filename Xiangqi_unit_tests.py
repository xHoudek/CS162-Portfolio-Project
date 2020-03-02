import XiangqiGame
import unittest


class MyTestCase(unittest.TestCase):
    def test_make_move(self):
        """tests basic legal move"""
        game = XiangqiGame.XiangqiGame()
        self.assertEqual(game.make_move('e1', 'e2'), True)

    def test_early_check(self):
        """tests game up to check"""
        game = XiangqiGame.XiangqiGame()
        move1 = game.make_move('b3', 'e3')
        move2 = game.make_move('h8', 'e8')
        move3 = game.make_move('h3', 'h6')
        move4 = game.make_move('b8', 'b4')
        move5 = game.make_move('e3', 'e7')  # black is in check
        self.assertEqual(game.is_in_check('black'), True)
        self.assertTrue(move1 and move2 and move3 and move4 and move5)

    def test_early_checkmate(self):
        """tests game up to checkmate"""
        game = XiangqiGame.XiangqiGame()
        game.make_move('b3', 'e3')
        game.make_move('h8', 'e8')
        game.make_move('h3', 'h6')
        game.make_move('b8', 'b4')
        game.make_move('e3', 'e7')  # black is in check
        move6 = game.make_move('e8', 'e4')
        self.assertEqual('UNFINISHED', game.get_game_state())

        move7 = game.make_move('h6', 'e6')  # black is checkmated here according to wikipedia

        self.assertEqual('RED_WON', game.get_game_state())  # currently says 'UNFINISHED'
        self.assertTrue(move6 and move7)

    def test_readme_example(self):
        """tests the code given in the readme"""
        game = XiangqiGame.XiangqiGame()
        move_result = game.make_move('c1', 'e3')
        black_in_check = game.is_in_check('black')
        game.make_move('e7', 'e6')
        state = game.get_game_state()

        self.assertEqual(True, move_result)
        self.assertEqual(False, black_in_check)
        self.assertEqual('UNFINISHED', state)

    def test_illegal_moves(self):
        """tests to make sure illegal moves return False"""
        game = XiangqiGame.XiangqiGame()
        self.assertFalse(game.make_move('e10', 'e9'))  # wrong turn
        self.assertFalse(game.make_move('a1', 'a4'))
        self.assertFalse(game.make_move('b1', 'd2'))
        self.assertFalse(game.make_move('d1', 'd2'))
        self.assertFalse(game.make_move('e1', 'd2'))
        self.assertFalse(game.make_move('a4', 'b4'))
        self.assertFalse(game.make_move('b3', 'b8'))


if __name__ == '__main__':
    unittest.main()
