# DS 5100 Final Project

**Project:** Monte Carlo Simulator  
**Name:** Tyler Gorecki

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


