import math
def color_probability(color, texture):

    prob=""
    
    if texture=="smooth":
        prob=str(math.floor((1/3)*100)/100)
           
    elif texture=="bumpy":
        if color=="red":
            prob=str(math.floor((4/7)*100)/100)
        elif color=="yellow":
            prob=str(math.floor((2/7)*100)/100)
        elif color=="green":
            prob=str(math.floor((1/7)*100)/100)
    return prob