def coor_r(x,y, team=True):
  x = (x+0.75)/1.5
  if not team:
    x = 1 - x
  
  y = 1-(y+0.65)/1.3
  return {"x":x,"y":y}

def support_position (data, Team):
    b1 = coor_r(data[f"{'B' if Team else 'Y'}1"]["x"],data[f"{'B' if Team else 'Y'}1"]["y"], team=Team)
    b2 = coor_r(data[f"{'B' if Team else 'Y'}2"]["x"],data[f"{'B' if Team else 'Y'}2"]["y"], team=Team)
    b3 = coor_r(data[f"{'B' if Team else 'Y'}3"]["x"],data[f"{'B' if Team else 'Y'}3"]["y"], team=Team)
    
    x_cor = {"b1": b1["x"], "b2": b2["x"], "b3": b3["x"]}
    y_cor = {"b1": b1["y"], "b2": b2["y"], "b3": b3["y"]}

    # checking for attacker and goalie
    if x_cor["b1"]==max(x_cor.values()):
        goalie_cor = {"x":x_cor["b1"],"y":y_cor["b1"]}
    if x_cor["b2"]==max(x_cor.values()):
        goalie_cor = {"x":x_cor["b2"],"y":y_cor["b2"]}
    if x_cor["b3"]==max(x_cor.values()):
        goalie_cor = {"x":x_cor["b3"],"y":y_cor["b3"]}
    if x_cor["b1"]==min(x_cor.values()):
        att_cor = {"x":x_cor["b1"],"y":y_cor["b1"]}
    if x_cor["b2"]==min(x_cor.values()):
        att_cor = {"x":x_cor["b2"],"y":y_cor["b2"]}
    if x_cor["b3"]==min(x_cor.values()):
        att_cor = {"x":x_cor["b3"],"y":y_cor["b3"]}

    #calculation of support optimal position
    #switch for colors 
    if Team:
        supp_opti_cor = {"x":att_cor["x"]+(goalie_cor["x"]-att_cor["x"])/(2),"y":0.5+(0.5-att_cor["y"])/(2)}
        if supp_opti_cor['x'] > 0.8:
            supp_opti_cor['x'] = 0.8
    else:
        supp_opti_cor = {"x":1-(att_cor["x"]+(goalie_cor["x"]-att_cor["x"])/(2)),"y":0.5+(0.5-att_cor["y"])/(2)}
        if supp_opti_cor['x'] < 0.2:
            supp_opti_cor['x'] = 0.2
    return supp_opti_cor
    