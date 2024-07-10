# DS 5100 Final Project

## Metadata

**Project:** Monte Carlo Simulator  
**Name:** Tyler Gorecki

## Synopsis

### Installation

To install this package, you can run this bash command in the directory of your choosing. 
```bash
pip install montecarlo
```

### Import

Import the montecarlo package in Python. The best way to do this for ease of use later on is the following: 

```python
from montecarlo.montecarlo import Die, Game, Analyzer
```

You can also call 'import montecarlo.montecarlo' in Python but must then call 'montecarlo.Die' (or similar calls for Game and Analyzer classes) when creating objects. 

### Create dice

Individual die objects are able to be created with default weights for each 'side' of 1, but that can also be modified. Create a six-sided die using the code below: 

```python
die = Die(np.array([1,2,3,4,5,6]))
coin.change_weight(1,3)
coin.current_die_state()
```

The code above creates an unfair die in which a one is three times more likely to appear than the rest of the numbers. This code also outputs each of the sides as well as their respective weights. 

### Play a game



```python
game = Game([die, die])
game.play(10)
game.show_recent_play()
```



### Analyze a game



```python
analyzer = Analyzer(game)
analyzer.jackpot()
analyzer.face_counts_per_roll()
analyzer.combo_count()
analyzer.permutation_count()
```


## API Description

### Die class

The die class contains the following methods and attributes: 

```python
class Die:
    """
    A Die is an object with N sides ('faces') and W weights and can be rolled to select 
    a face. By default, each of the sides have a weight of 1, but that can be changed using 
    a method in this class to adjust individual sides. Each side is unique and the Die object can be rolled one or more times, resulting in a single face for each roll. 
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
```

### Game class

The game class contains the following methods and attributes: 

```python
class Game:
    """
    A Game object consists of rolling one or more similar Die objects one or more times. 
    The dice should be similar, meaning they have the same number of sides and associated 
    faces, and Game objects only keep the results of their most recent play. The one attribute of the class is a list of the Die objects the game contains. 
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

    def play(self, rolls):
        """
        This method takes an integer parameter to specify the number of times the dice 
        should be rolled. These values are then saved in a private data frame in wide 
        format. The roll number is named index starting with 0 and each die index is the 
        column name, with the values being faces rolled for each instance. 

        Parameters
        ----------
        rolls : number of rolls to perform on each Die object within the Game object

        Returns
        -------
        None
        """

    def show_recent_play(self, df_form = 'wide'):
        """
        Returns a copy of the private data frame created by the play function to the user. 
        Takes a parameter that controls whether the data frame is returned in narrow or 
        wide form. 

        Parameters
        ----------
        df_form : must be a string value in {'narrow', 'wide'}, default is 'wide'

        Returns
        -------
        Narrow or wide formed data frame consisting of the data from the most recent play 
        function call by the Game object

        Raises
        ------
        ValueError
            when df_form input is not one of 'narrow' or 'wide'
        """
```

### Analyzer class

The analyzer class contains the following methods and attributes: 

```python
class Analyzer:
    """
    An Analyzer object takes the result of a Game object and computes various descriptive 
    statistical properties about it. The one attribute of the class is the Game object itself. 
    """

    def __init__(self, game):
        """
        Initializes an Analyzer object from a Game object input. 

        Parameters
        ----------
        game : must be a Game object

        Returns
        -------
        None

        Raises
        ------
        ValueError
            when input parameter is not a Game object
        """

    def jackpot(self):
        """
        A jackpot is a result in which all faces are the same for each roll of all dice in
        the game. This method computes how many times this occurs among all rolls in the game. 

        Parameters
        ----------
        None

        Returns
        -------
        An integer for the number of jackpots. 
        """

    def face_counts_per_roll(self):
        """
        Computes the number of times each face is rolled in each event, returning a data 
        frame of the results. 

        Parameters
        ----------
        None

        Returns
        -------
        Data frame in wide format containing roll number as index, face values as columns, 
        and count values in the cells. 
        """

    def combo_count(self):
        """
        Computes the distinct combinations of faces rolled and their counts. Here, the order 
        does not matter. The method returns a data frame of the results. 

        Parameters
        ----------
        None

        Returns
        -------
        Data frame with a MultiIndex of distinct combinations and a column for the associated 
        counts values. 
        """

    def permutation_count(self):
        """
        Computes the distinct permutations of faces rolled and their counts. Here, the order 
        does matter. The method returns a data frame of the results. 
        

        Parameters
        ----------
        None

        Returns
        -------
        Data frame with a MultiIndex of distinct permutations and a column for the associated 
        count values. 
        """
```