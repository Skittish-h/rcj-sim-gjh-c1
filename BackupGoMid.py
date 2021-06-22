import math

class lackOfProgress:
    def __init__(self,tre) -> None:
        TIME_STEP = 64
        self.steps = math.ceil(5/(TIME_STEP/1000.0)) 
        self.threshold = tre
        self.samples = [0 for x in range(self.steps)]
        self.iterator = 0
        self.prev_position= None

    def isLackOfProgress(self,ballpos): 
        if self.prev_position == None:
            self.prev_position = ballpos

        change = math.sqrt((self.prev_position["x"] - ballpos["x"]) ** 2 +
                          (self.prev_position["y"] - ballpos["y"]) ** 2)

        self.samples[self.iterator % self.steps] = change
        self.iterator += 1
        self.prev_position = ballpos

        changeSum = sum(self.samples)
        return (changeSum>=self.threshold)

    def midPos(team, ball_pos):
        if(team):
            mid_pos = {"x":(0.8 if ball_pos['x'] > 0.5 else 0.48),"y":0.5}
        else:
            mid_pos = {"x":(0.2 if ball_pos['x'] < 0.5 else 0.52),"y":0.5}
        return mid_pos
