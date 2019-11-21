import unittest
from BowlingGame import Game


class BowlingGameTestCase(unittest.TestCase):
    game = None

    def setUp(self):
        self.game = Game()

    def manyLoop(self, nb_roll, pins):
        for _ in range(nb_roll):
            self.game.roll(pins)

    def testGutterGame(self):
        self.manyLoop(20, 0)
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        self.manyLoop(20, 1)
        self.assertEqual(20, self.game.score())

if __name__ == '__main__':
    unittest.main()
