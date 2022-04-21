# Snake

The project focuses on the artificial intelligence of the [Snake][snake-wiki] game. The snake's goal is to eat the food continuously and fill the map with its bodies as soon as possible. Originally, the project was [written in C++][snake-cpp]. It has now been rewritten in Python for a user-friendly GUI and the simplicity in algorithm implementations.

***[Algorithms >][doc-algorithms]***

## Experiments

We use two metrics to evaluate the performance of an AI:

1. **Average Length:** Average length the snake has grown to (*max:* 64).
2. **Average Steps:** Average steps the snake has moved.

Test results (averaged over 1000 episodes):

| Solver | Demo (optimal) | Average Length | Average Steps |
| :----: | :------------: | :------------: | :-----------: |
|[Hamilton][doc-hamilton]|![][demo-hamilton]|63.93|717.83|
|[Greedy][doc-greedy]|![][demo-greedy]|60.15|904.56|
|[DQN][doc-dqn]<br>(experimental)|![][demo-dqn]|24.44|131.69|

## Installation

Requirements: Python 3.5+ (64-bit) with [Tkinter][doc-tkinter] installed.

```
pip install -r requirements.txt
python run.py [-h]
```

Run unit tests:

```
python -m pytest -v
```
