import copy
import random


class Hat:

  def __init__(self, **hats):
    self.contents = list()
    for key, val in hats.items():
      for i in range(val):
        self.contents.append(key)
    #print('original hat', self.contents)
  def draw(self, num):
    if len(self.contents) <= num:
      return self.contents
    else:
      drawn_balls = list()
      for j in range(num):
        drawn = random.sample(
            self.contents, 1
        )  #can also use choices(), randrange(), randint() giving the same result
        drawn_balls += drawn
        for item in drawn:
          if item in self.contents:
            self.contents.remove(item)

      return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  event = 0
  for experiment in range(num_experiments):
    expected = list()
    for c, n_ball in expected_balls.items():
      for color in range(n_ball):
        expected.append(c)
    new_hat = copy.deepcopy(hat)
    sample_list = new_hat.draw(num_balls_drawn)

    for color in sample_list:
      if color in expected:
        expected.remove(color)
    if len(expected) == 0:
      event += 1

    probability = event / num_experiments
  return probability
