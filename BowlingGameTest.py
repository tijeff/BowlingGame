import unittest
from BowlingGame import Game


class BowlingGameTestCase(unittest.TestCase):
    game = None

    def setUp(self):
        self.game = Game()

    def manyLoop(self):
        for _ in range(20):
            self.game.roll(0)

    def testGutterGame(self):
        self.manyLoop()
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        for _ in range(20):
            self.game.roll(1)
        self.assertEqual(20, self.game.score())

if __name__ == '__main__':
    unittest.main()
