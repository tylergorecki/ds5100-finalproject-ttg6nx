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

Die objects are able to be created with default weights for each 'side' of 1, but that can be modified. 

```python
die = Die(np.array(['H','T']))
die.change_weight('H',3)
die.current_die_state()
```

The code above creates an unfair coin in which heads is three times more likely to appear than tails. 