import numpy as np
import pandas as pd

class Die:
    """DOCSTRING"""

    def __init__(self, face_values):
        """DOCSTRING"""
    
        if type(face_values) != type(np.array(1)):
            raise TypeError("Faces is not a numpy array")
        
        if len(face_values) != len(np.unique(face_values)):
            raise ValueError("Faces does not have all unique values")
        
        self._die = pd.DataFrame(data = {
            'face': face_values, 
            'weights': np.ones(len(face_values))
        }).set_index('face')
        
    def change_weight(self, face, new_val):
        """DOCSTRING"""

        if face not in self._die.index:
            raise IndexError("Face value not in die array")
        
        if type(new_val) not in [int, float]:
            try:
                new_val = float(new_val)
            except:
                raise TypeError("The new value is not numeric or castable as numeric")

        
        self._die.loc[face] = new_val

    def roll(self, rolls = 1):
        """DOCSTRING"""

        weights = self._die.weights/sum(self._die.weights)

        return list(np.random.choice(
            a = self._die.index, 
            size = rolls, 
            p = weights
        ))

    def current_die_state(self):
        """DOCSTRING"""

        return self._die.copy()


class Game:
    """DOCSTRING"""

    def __init__(self, dice):
        """DOCSTRING"""

        # OPTIONAL PORTION

        self.dice = dice

    def play(self, rolls):
        """DOCSTRING"""

        self._play_dice = pd.DataFrame({
            die_num : die_obj.roll(rolls) for die_num, die_obj in enumerate(self.dice)
        })

    def show_recent_play(self, df_form = 'wide'):
        """DOCSTRING"""

        if df_form not in ['wide', 'narrow']:
            raise ValueError("Form invalid, input must be 'narrow' or 'wide'")

        if df_form == 'wide':
            return self._play_dice.copy()
        else:
            return self._play_dice.stack().to_frame('Outcome').rename_axis(['Roll', 'Die'])


class Analyzer:
    """DOCSTRING"""

    def __init__(self, game):
        """DOCSTRING"""

        if type(game) != Game:
            raise ValueError("Input parameter is not a game object")

        self.game = game

    def jackpot(self):
        """DOCSTRING"""

        return sum(self.game.show_recent_play().nunique(axis = 0) == 1)

    def face_counts_per_roll(self):
        """DOCSTRING"""

        return self.game.show_recent_play().apply(pd.Series.value_counts, axis = 1).fillna(0).astype(int)

    def combo_count(self):
        """DOCSTRING"""
        
        df = self.game.show_recent_play()
        new_df = pd.DataFrame([sorted(df.iloc[x]) for x in range(len(df))])
        cols = list(new_df.columns)

        return new_df.groupby(cols).size().reset_index(name = 'Count').set_index(cols)

    def permutation_count(self):
        """DOCSTRING"""

        df = self.game.show_recent_play()
        cols = list(df.columns)

        return df.groupby(cols).size().reset_index(name = 'Count').set_index(cols)
        
