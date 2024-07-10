from montecarlo.montecarlo import Die, Game, Analyzer
import unittest
import numpy as np
import pandas as pd

class MontecarloTest(unittest.TestCase):

    def test_die_init(self):
        die1 = Die(np.array(['A','B','C']))

        self.assertTrue(all(die1.current_die_state().weight == 1))

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
        actual = list(die1.current_die_state().index)
        expected = ['A','B','C']

        self.assertEqual(actual, expected)

    def test_game_init(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        self.assertEqual(die1, game.dice[0])

    def test_game_play(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game.play(5)
        recent_game = game.show_recent_play()

        actual = recent_game.shape[0]
        expected = 5

        self.assertEqual(actual, expected)

    def test_game_show_play(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game.play(5)
        recent_game = game.show_recent_play('narrow')

        self.assertTrue(type(recent_game.index) == pd.MultiIndex)

    def test_analyzer_init(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game.play(5)
        analyzer1 = Analyzer(game)

        self.assertTrue(type(analyzer1.face_counts_per_roll()) == pd.DataFrame)

    def test_analyzer_jackpot(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game._play_dice = pd.DataFrame({
            0: ['A','A','B'], 
            1: ['A','B','B'], 
            2: ['A','C','B']
        })

        analyzer = Analyzer(game)
        actual = analyzer.jackpot()
        expected = 2
        self.assertEqual(actual, expected)

    def test_analyzer_face_counts_per_roll(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game._play_dice = pd.DataFrame({
            0: ['A','A','A'], 
            1: ['A','B','C'], 
            2: ['B','B','B']
        })

        analyzer = Analyzer(game)
        actual = list(analyzer.face_counts_per_roll().loc[2])
        expected = [1,1,1]
        self.assertEqual(actual, expected)


    def test_analyzer_combo_count(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game._play_dice = pd.DataFrame({
            0: ['B','A','B'], 
            1: ['A','B','C'], 
            2: ['B','B','B']
        })

        analyzer = Analyzer(game)
        actual = analyzer.combo_count()

        expected = pd.DataFrame({
            'Count':[2,1]
        }, index=pd.MultiIndex.from_tuples([('A','B','B'), ('B','B','C')], names=[0,1,2]))

        self.assertEqual(actual.shape, expected.shape)


    def test_analyzer_permutation_count(self):
        die1 = Die(np.array(['A','B','C']))
        die2 = Die(np.array(['A','B','C']))
        die3 = Die(np.array(['A','B','C']))
        game = Game([die1, die2, die3])

        game._play_dice = pd.DataFrame({
            0: ['C','A','A'], 
            1: ['C','B','B'], 
            2: ['B','B','B']
        })

        analyzer = Analyzer(game)
        actual = list(analyzer.permutation_count()['Count'])
        expected = [2,1]

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=3)