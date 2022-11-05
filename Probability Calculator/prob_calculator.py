import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, val in kwargs.items() for _ in range(val)]
        self.drawn = []

    def __str__(self):
        return str(self.contents)

    def draw(self, balls):
        if balls > len(self.contents):
            return self.contents
        else:
            self.drawn = random.sample(self.contents, int(balls))
        for element in self.drawn:
            if element in self.contents:
                self.contents.remove(element)
            else:
                return self.contents
        return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    for key, val in expected_balls.items():
        for _ in range(val):
            expected.append(key)
    i = 0
    m = 0  
    while i < num_experiments:
        origin_hat = copy.deepcopy(hat)
        if all(item in origin_hat.draw(num_balls_drawn) for item in expected) is True:
            m += 1
            i += 1
        else:
            i += 1
    return m / num_experiments
