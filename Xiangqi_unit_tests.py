import XiangqiGame
import unittest


class MyTestCase(unittest.TestCase):
    def test_make_move(self):
        game = XiangqiGame.XiangqiGame()
        self.assertEqual(game.make_move('e1', 'e2'), True)

    def test_early_check(self):
        game = XiangqiGame.XiangqiGame()
        game.make_move('b3', 'e3')
        game.make_move('h8', 'e8')
        game.make_move('h3', 'h6')
        game.make_move('b8', 'b4')
        game.make_move('e3', 'e7')  # black is in check
        self.assertEqual(game.is_in_check('black'), True)

    def test_early_checkmate(self):
        game = XiangqiGame.XiangqiGame()
        game.make_move('b3', 'e3')
        game.make_move('h8', 'e8')
        game.make_move('h3', 'h6')
        game.make_move('b8', 'b4')
        game.make_move('e3', 'e7')  # black is in check
        game.make_move('e8', 'e4')
        game.make_move('h6', 'e6')  # black is checkmated here according to wikipedia

        self.assertEqual('RED_WON', game.get_game_state())  # currently says 'UNFINISHED'


if __name__ == '__main__':
    unittest.main()
