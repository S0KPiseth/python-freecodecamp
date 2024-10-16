import copy
import random

class Hat:
    def __init__(self, **kwarg):
        self.kwarg = kwarg
        self.contents = []
        for index, key in enumerate(kwarg.keys()):
            for occur in range(list(kwarg.values())[index]):
                self.contents.append(key)
        self.contents_copy = copy.deepcopy(self.contents)

    def draw(self, numd):
        final_answer = []
        
        self.contents = copy.deepcopy(self.contents_copy)
        if numd < len(self.contents_copy):
            for _ in range(numd):
                choice = random.choice(self.contents)
                final_answer.append(choice)
                self.contents.remove(choice)
            return final_answer
        else:
        
            self.contents.clear()
            return self.contents_copy

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for key, occur in expected_balls.items():
        expected_balls_list.extend([key] * occur)  

    expected_count = 0

    for _ in range(num_experiments):
        temp_result = hat.draw(num_balls_drawn)
        
       
        temp_result_dict = {k: temp_result.count(k) for k in set(temp_result)}
        
        match = True
        
        for key, value in expected_balls.items():
            if temp_result_dict.get(key, 0) < value:
                match = False
                break

        if match:
            expected_count += 1

    return expected_count / num_experiments

hat = Hat(black=6, red=4, green=3)

print(experiment(hat=hat,
                  expected_balls={'red': 2, 'green': 1},
                  num_balls_drawn=5,
                  num_experiments=2000))