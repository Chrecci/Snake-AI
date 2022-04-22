## README

A python snake-AI solver based on the following repository: https://github.com/chuyangliu/snake 

Borrowing the general class structures, and GUI, I implemented an original A* search algorithm based on a Manhattan-Distance heuristic. A few other things involving testing, speed, configurations are also modified. The AI works very well, and is shockingly cute. Installation instructions are provided below. Upon launching the interface, the snake will immediately begin to run it's course. The slider controls the speed of the AI, and space bar to pause. Hope you enjoy! 

## Metrics

Running report.ipynb independently will generate graphs summarizing overall statistics of each approach. The ideal solution is still hamiltonian cycle since it's pretty much a perfect solution, but more often than not, A* performance just nudges out greedy. Frontier size is also an additional metric that I inserted, which tracks the maximum number of nodes stored in queues for exploration.

## Installation and Commands

Requirements: Python 3.5+ (64-bit) with Tkinter installed.

Install dependencies  
```
pip install -r requirements.txt
```

Run default (default A* search): 
```
python run.py
```
To run another algorithm, use -s flag.  

Run benchmark (default A* search): 
```
python run.py -m bmck
```

Run unit tests:

```
python -m pytest -v
```
