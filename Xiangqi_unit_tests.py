import unittest, XiangqiGame


class MyTestCase(unittest.TestCase):
    def test_make_move(self):
        game = XiangqiGame.XiangqiGame()
        self.assertEqual(game.make_move('e1', 'e2'), True)


if __name__ == '__main__':
    unittest.main()
