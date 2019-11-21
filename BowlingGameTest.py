import unittest
from BowlingGame import Game


class BowlingGameTestCase(unittest.TestCase):
    game = None

    def setUp(self):
        self.game = Game()

    def manyLoop(self, nb_roll, pins):
        for _ in range(nb_roll):
            self.game.roll(pins)

    def rollSpare(self):
        self.game.roll(4)
        self.game.roll(6)

    def testGutterGame(self):
        self.manyLoop(20, 0)
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        self.manyLoop(20, 1)
        self.assertEqual(20, self.game.score())

    def testSpare(self):
        self.rollSpare()
        self.game.roll(3)
        self.manyLoop(17, 0)
        self.assertEqual(16, self.game.score())  # 10 + 2*3

    def testStrike(self):
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.manyLoop(16, 0)
        self.assertEqual(24, self.game.score())


if __name__ == '__main__':
    unittest.main()
