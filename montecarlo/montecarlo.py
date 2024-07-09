import numpy as np
import pandas as pd

class Die:
    """
    A Die is an object with N sides ('faces') and W weights and can be rolled to select 
    a face. By default, each of the sides have a weight of 1, but that can be changed using 
    a method in this class to adjust individual sides. Each side is unique and the Die object 
    can be rolled one or more times, resulting in a single face for each roll. 
    """

    def __init__(self, face_values):
        """
        Initializes a Die object and saves the faces and weights of the Die in a private data 
        frame with faces as the index. 

        Parameters
        ----------
        face_values : must be a numpy array of all unique values

        Returns
        -------
        None

        Raises
        ------
        TypeError
            when face_values input is not a numpy array
        ValueError
            when face_values input does not have all unique values
        """
    
        if type(face_values) != type(np.array(1)):
            raise TypeError("Faces is not a numpy array")
        
        if len(face_values) != len(np.unique(face_values)):
            raise ValueError("Faces does not have all unique values")
        
        self._die = pd.DataFrame(data = {
            'face': face_values, 
            'weight': np.ones(len(face_values))
        }).set_index('face')
        
    def change_weight(self, face, new_val):
        """
        This method changes the weight of a single side. It takes a face and a numeric value 
        as inputs, saving that face's new weight value in the Die's private data frame. 

        Parameters
        ----------
        face : face value (side) of the Die to be changed
        new_val : new weight value for that face, must be numeric or castable to numeric

        Returns
        -------
        None

        Raises
        ------
        IndexError
            when face argument is not a face value in the current Die object
        TypeError
            when new_val input is not a numeric or a string castable to numeric
        """

        if face not in self._die.index:
            raise IndexError("Face value not in die array")
        
        if type(new_val) not in [int, float]:
            try:
                new_val = float(new_val)
            except:
                raise TypeError("The new value is not numeric or castable as numeric")

        
        self._die.loc[face] = new_val

    def roll(self, rolls = 1):
        """
        Rolls the Die one or more times. Randomly samples n (number of rolls input) times 
        and returns the face results of the rolls as a list. 

        Parameters
        ----------
        rolls : default is 1, indicates the number of rolls to sample from the Die object

        Returns
        -------
        List of face outputs that result from the random sampling of the Die object. 
        """

        weights = self._die.weight/sum(self._die.weight)

        return list(np.random.choice(
            a = self._die.index, 
            size = rolls, 
            p = weights
        ))

    def current_die_state(self):
        """
        Shows the Die object's current state by returning a copy of the private die data frame. 

        Parameters
        ----------
        None

        Returns
        -------
        The private data frame containing face values and weights for each face of the Die object. 
        """

        return self._die.copy()


class Game:
    """
    A Game object consists of rolling one or more similar Die objects one or more times. 
    The dice should be similar, meaning they have the same number of sides and associated 
    faces, and Game objects only keep the results of their most recent play. 
    """

    def __init__(self, dice):
        """
        Initializes a Game object, created from a list of similar dice. The dice should 
        have the same faces. 

        Parameters
        ----------
        dice : must be a list of already instantiated similar dice

        Returns
        -------
        None
        """

        self.dice = dice

    def play(self, rolls):
        """
        

        Parameters
        ----------
        rolls : number of rolls to perform on each Die object within the Game object

        Returns
        -------
        None
        """

        self._play_dice = pd.DataFrame({
            die_num : die_obj.roll(rolls) for die_num, die_obj in enumerate(self.dice)
        })

    def show_recent_play(self, df_form = 'wide'):
        """
        

        Parameters
        ----------
        df_form : must be a string value in {'narrow', 'wide'}

        Returns
        -------
        Narrow or wide formed data frame consisting of the data from the most recent play() 
        function call by the Game object

        Raises
        ------
        ValueError
            when df_form input is not one of 'narrow' or 'wide'
        """

        if df_form not in ['wide', 'narrow']:
            raise ValueError("Form invalid, input must be 'narrow' or 'wide'")

        if df_form == 'wide':
            return self._play_dice.copy()
        else:
            return self._play_dice.stack().to_frame('Outcome').rename_axis(['Roll', 'Die'])


class Analyzer:
    """
    
    """

    def __init__(self, game):
        """
        Initializes an Analyzer object

        Parameters
        ----------
        game : must be a Game object

        Returns
        -------
        None

        Raises
        ------
        ValueError
            when input parameter is not a game object
        """

        if type(game) != Game:
            raise ValueError("Input parameter is not a game object")

        self.game = game

    def jackpot(self):
        """
        

        Parameters
        ----------
        None

        Returns
        -------
        
        """

        df = self.game.show_recent_play()

        return sum(df.nunique(axis = 0) == 1)

    def face_counts_per_roll(self):
        """
         

        Parameters
        ----------
        None

        Returns
        -------
        
        """

        df = self.game.show_recent_play()

        return df.apply(pd.Series.value_counts, axis = 1).fillna(0).astype(int)

    def combo_count(self):
        """
        

        Parameters
        ----------
        None

        Returns
        -------
        
        """
        
        df = self.game.show_recent_play()
        new_df = pd.DataFrame([sorted(df.iloc[x]) for x in range(len(df))])
        cols = list(new_df.columns)

        return new_df.groupby(cols).size().reset_index(name = 'Count').set_index(cols)

    def permutation_count(self):
        """
        

        Parameters
        ----------
        None

        Returns
        -------
        
        """

        df = self.game.show_recent_play()
        cols = list(df.columns)

        return df.groupby(cols).size().reset_index(name = 'Count').set_index(cols)
        
