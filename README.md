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