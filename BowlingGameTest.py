import unittest
from BowlingGame import Game


class BowlingGameTestCase(unittest.TestCase):
    def testGutterGame(self):
        game = Game()
        for _ in range(20):
            game.roll(0)
        self.assertEqual(0, game.score())

if __name__ == '__main__':
    unittest.main()
