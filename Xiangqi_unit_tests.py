import XiangqiGame
import unittest


class MyTestCase(unittest.TestCase):
    def test_make_move(self):
        game = XiangqiGame.XiangqiGame()
        self.assertEqual(game.make_move('e1', 'e2'), True)

    def test_early_check(self):
        game = XiangqiGame.XiangqiGame()
        move1 = game.make_move('b3', 'e3')
        move2 = game.make_move('h8', 'e8')
        move3 = game.make_move('h3', 'h6')
        move4 = game.make_move('b8', 'b4')
        move5 = game.make_move('e3', 'e7')  # black is in check
        self.assertEqual(game.is_in_check('black'), True)
        self.assertTrue(move1 and move2 and move3 and move4 and move5)

    def test_early_checkmate(self):
        game = XiangqiGame.XiangqiGame()
        game.make_move('b3', 'e3')
        game.make_move('h8', 'e8')
        game.make_move('h3', 'h6')
        game.make_move('b8', 'b4')
        game.make_move('e3', 'e7')  # black is in check
        move6 = game.make_move('e8', 'e4')
        move7 = game.make_move('h6', 'e6')  # black is checkmated here according to wikipedia

        self.assertEqual('RED_WON', game.get_game_state())  # currently says 'UNFINISHED'
        self.assertTrue(move6 and move7)

    def test_readme_example(self):
        game = XiangqiGame.XiangqiGame()
        move_result = game.make_move('c1', 'e3')
        black_in_check = game.is_in_check('black')
        game.make_move('e7', 'e6')
        state = game.get_game_state()

        self.assertEqual(True, move_result)
        self.assertEqual(False, black_in_check)
        self.assertEqual('UNFINISHED', state)


if __name__ == '__main__':
    unittest.main()
