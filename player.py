import random

class Player3d():
    def __init__(self, left_prob, right_prob):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.left_prob = left_prob
        self.right_prob = right_prob
    
    def random_walk(self):

        choose_axis = random.randint(1, 3)
        random_percent = random.random()
        
        match choose_axis:
            case 1:
                if random_percent < self.left_prob:
                    self.pos_x -= 1
                else:
                    self.pos_x += 1
            case 2:
                if random_percent < self.left_prob:
                    self.pos_y -= 1
                else:
                    self.pos_y += 1
            case 3:
                if random_percent < self.left_prob:
                    self.pos_z -= 1
                else:
                    self.pos_z += 1

    def __str__(self):
        return f"Pos X: {self.pos_x}, Y: {self.pos_y}, Z: {self.pos_z}"
    


class Player2d():
    def __init__(self, left_prob, right_prob):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.left_prob = left_prob
        self.right_prob = right_prob
    
    def random_walk(self):

        choose_axis = random.randint(1, 2)
        random_percent = random.random()
        
        match choose_axis:
            case 1:
                if random_percent < self.left_prob:
                    self.pos_x -= 1
                else:
                    self.pos_x += 1
            case 2:
                if random_percent < self.left_prob:
                    self.pos_y -= 1
                else:
                    self.pos_y += 1

    def __str__(self):
        return f"Pos X: {self.pos_x}, Y: {self.pos_y}"
    
class Player1d():
    def __init__(self, left_prob, right_prob):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.left_prob = left_prob
        self.right_prob = right_prob
    
    def random_walk(self):

        random_percent = random.random()
        
        if random_percent < self.left_prob:
            self.pos_x -= 1
        else:
            self.pos_x += 1


    def __str__(self):
        return f"Pos X: {self.pos_x}"
                
    