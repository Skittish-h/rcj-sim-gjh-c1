import math

def goalie_angles(ball_pos: dict):

    #return the angle at which the robot should rotate to face the ball

    #blue = {'x': 0.73, 'yr': -0.105,  'yc': 0, 'yl': 0.105 }
    blue = {'x': 0.986666666, 'yr': 0.580769,  'yc': 0.5, 'yl': 0.4192307 }

    if (ball_pos['y'] >= 0.105):

        angle_center = math.atan2(
        ball_pos['x'] - blue['x'],
        ball_pos['y'] - blue['yl'],
        )

    elif(ball_pos['y']<= -0.105):

        angle_center = math.atan2(
        ball_pos['x'] - blue['x'],
        ball_pos['y'] - blue['yr'],
        )

    elif(ball_pos['y']> -0.105 and ball_pos['y']<0.105):

        angle_center = math.atan2(
            ball_pos['x']- blue['x'],
            ball_pos['y']-blue['yc'])

    
    return angle_center


def correct_rotation(robot_pos: dict, angle):
    right_speed = 0
    left_speed = 0
    if(angle <-1.7 and angle<-1.5):
        right_speed = 0
        left_speed = 0

    elif(angle > -1.5):
        right_speed = 5
        left_speed = -5

    elif(angle<-1.5):
        right_speed = -5
        left_speed = 5

    return(right_speed, left_speed)




def goalie_cal_Y(ball_pos: dict):
    #calculates ration between the outer goal shit and the entire field and returns the Y
    if (ball_pos['y']>0.5):
        goalie_Y = (ball_pos['y']/1.066) + 0.02

    elif(ball_pos['y'] > 0.47 and ball_pos['y'] < 0.52):
        goalie_Y = 0.5

    else:
        goalie_Y = 1.2/(1.066/ball_pos['y']) + 0.02

    
    if (goalie_Y>0.7):
        goalie_Y = 0.7
    elif (goalie_Y<0.26):
        goalie_Y = 0.28

    return goalie_Y


#def move_to_X(robot_pos: dict):
    #if (robot_pos['x'] < 0.58):
     #   left_speed = 5
    #    right_speed = 5
   # elif (robot_pos['x'] > 0.58):
  #      left_speed = 0
 #       right_speed = 0
#    return left_speed, right_speed


ball_pos = {'x': 0.5, 'y': 0.3}

goalie_cal_Y(ball_pos)

intercepts = {"b1": 0,"b2": 0,"b3": 0}
intercepts["b1"] = 4
intercepts["b2"] = 5
intercepts["b3"] = 6

x = "b1"


