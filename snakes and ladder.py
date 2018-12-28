import fileinput
from random import random

class Board:
  def __init__(self, slides):
    self.current = 1
    self.slides = {}
    for p in slides:
      start, end = [int(x) for x in p.split(",")]
      self.slides[start] = end
    
  def move(self, num):
    if self.current + num <= 100:
      self.current += num
    if self.current in self.slides:
      self.current = self.slides[self.current]
    return self.current

class Die:
  def __init__(self, probs):
    self.probs = [float(x) for x in probs]
   def roll(self):
    rand = random()
    for index, prob in enumerate(self.probs):
      if rand < prob:
        return index + 1
      rand -= prob
    return 6

def play(probs, ladders, snakes):
  board = Board(ladders + snakes)
  die = Die(probs)
  num_moves = 0
  while num_moves < 1000 and board.move(die.roll()) != 100:
    num_moves += 1
  return num_moves

def parse_params():
  lines = fileinput.input()
  num_tests = int(lines[0])
  tests = []
  i = 0
  while i < num_tests:
    probs = lines[4*i + 1].strip().split(",")
    num_ladders, num_snakes = lines[4*i + 2].strip().split(",")
    ladder_starts = lines[4*i + 3].strip().split(" ")
    snake_starts = lines[4*i + 4].strip().split(" ")
    tests.append([probs, ladder_starts, snake_starts])
    i += 1
  return tests

def main():
  tests = parse_params()
  for params in tests:
    sum = 0
    num_trials = 0
    for i in range(5000): # 5000 trials
      num_moves = play(*params)
      if num_moves < 1000:
        sum += num_moves
        num_trials += 1
    print (sum / num_trials)

if __name__ == "__main__":
  main()
