from montecarlo.montecarlo import Die, Game, Analyzer
import unittest
import numpy as np

class MontecarloTest(unittest.TestCase):

    def test_die_init(self):
        die1 = Die(np.array(['A','B','C']))
        self.assertTrue(all(die1.current_die_state().weights == 1))
        print('reached here 1')

    def test_die_change_weight(self):
        die1 = Die(np.array(['A','B','C']))
        die1.change_weight('B',2)
        actual = die1.current_die_state().loc['B'].weight
        expected = 2
        self.assertEqual(actual, expected)

    def test_die_roll(self):
        die1 = Die(np.array(['A','B','C']))
        self.assertTrue(type(die1.roll(10)) == list)

    def test_die_state(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        self.assertEqual(die1.current_die_state(), die2.current_die_state())
        print('reached here 2')

    def test_game_init(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        self.assertEqual(die1, game1.dice[0])

    def test_game_play(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        try:
            game1.play(5)
        except Exception as e:
            print("There is an error")

    def test_game_show_play(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        game1.play(5)
        recent_game = game1.show_recent_play()
        pass

    def test_analyzer_init(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

    def test_analyzer_jackpot(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

    def test_analyzer_jackpot(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

    def test_analyzer_face_counts(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

    def test_analyzer_combo_count(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

    def test_analyzer_permutation_count(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game1 = Game([die1, die2, die3])
        analyzer1 = Analyzer(game1)
        pass

if __name__ == '__main__':
    unittest.main(verbosity=3)