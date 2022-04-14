import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):

    def test_die_by_underpopulation(self):
        # Test rule 1. Any live cell with fewer than two live neighbours dies,
        # as if by underpopulation.
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run("-3,-5 -4,-5 -5,-5")

        output = fake_stdout.getvalue()
        fake_stdout.close()

        # Should all die because they each only have 1 neighbor.
        self.assertEqual(output, "-4,-5")
