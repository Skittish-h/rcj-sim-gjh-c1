# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils

from intercepts import interceptCalculator
from CoordinateRecalculator import coor_recalc, robot_pos_recalc
from GoToFunc import goTo

from MovementCalculator import fit_parabola, get_tangent_point, passes_boundary, scores_own_goal
from BackupGoMid import lackOfProgress

######

INTERCEPT_CONST = 0.03

# Feel free to import built-in libraries
import math
#robot class
class MyRobot(RCJSoccerRobot):
    
    #function that uses instacne of intercept calculator to find our robots intercepts and the intercepts for all
    def getIntercepts(self, data, Team):
        #get our robots
        r1 = robot_pos_recalc(data[f"{self.team}{self.player_id}"], Team=Team)

        #prep dictionary
        intercepts = {"r1":0,"r2":0 ,"r3":0}
        
        #get all the intercepts, with a lota samples
        intercept = self.intercept_c.calculateOptimumIntercept(r1, Team, sample_count=200)
        

        #dict with times

        #dict with our robots intercepts

        return intercept
    
   

    def be_attacker(self, myi, robot_pos, team):
        stuff = 0
        point = 0
        if (myi['x'] < robot_pos['x']) if team else (myi['x'] > robot_pos['x']):
            
            #print(intercepts)
            x = fit_parabola(myi, robot_pos ,{'x':(0.0 if team else 1.0),"y":0.5})
            if not passes_boundary(x):
                point = get_tangent_point(robot_pos, x, team)
                ball_angle, robot_angle = self.get_angles(point, robot_pos)
                
                return goTo(point['x'], point['y'], robot_pos, robot_angle, should_soften=False)
                
            else:
                ball_angle, robot_angle = self.get_angles(myi, robot_pos)
                
                return goTo(myi['x'], myi['y'], robot_pos, robot_angle, should_soften=False)
                
        else:
            ball_angle, robot_angle = self.get_angles(myi, robot_pos)
            
            return goTo(myi['x'], myi['y'], robot_pos, robot_angle, should_soften=False)
        



    def run(self):
        #create interceptcalc instance
        self.intercept_c = interceptCalculator(3)
        lackOfProgCheck = lackOfProgress(0.35)
        
        
        Team = (self.team == "B")
        while self.robot.step(TIME_STEP) != -1:

            if self.is_new_data():
                data = self.get_new_data()
                #due to extensive openAI gym testing we know that desync DOES occur
                while self.is_new_data():            
                    data = self.get_new_data()
                robot_pos = robot_pos_recalc(data[self.name], Team)
                # Get & recalculate the position of the ball
                ball_pos = coor_recalc(data['ball']['x'], data['ball']['y'], Team)
                self.intercept_c.pushPoint(ball_pos)
                
                myi = self.getIntercepts(data, Team)
                
                
                #role = self.role_decision(intercepts, data)
                

                out=[]

                #backup_goMid= lackOfProgCheck.isLackOfProgress(ball_pos)

                # if roles att is 1 the B1 will execute attacker code
                #if role == "att":                
                out = self.be_attacker(myi, robot_pos, Team)

                # if goalie will be 1 B1 will execute goalie code
                #elif role == "goal":

                #if support is 1 B1 will execute backup code
                #elif role == "back":
                #    out = self.be_backup(backup_goMid, robot_pos, data, ball_pos, Team)
                 #   pass
                #if our action would result in us shooting towards our own goal overwrite the action
                # if scores_own_goal((1.0 if Team else 0.0), ball_pos, robot_pos, Team):
                #     print("AAA")
                #     target_pos = self.intercept_c.ball_doge_pos(ball_pos, robot_pos)
                #     ball_angle, robot_angle = self.get_angles(target_pos, robot_pos)
                #     out = goTo(target_pos["x"], target_pos["y"], robot_pos, robot_angle)


                self.left_motor.setVelocity(out[1])
                self.right_motor.setVelocity(out[0])
               
                
my_robot = MyRobot()
my_robot.run()
