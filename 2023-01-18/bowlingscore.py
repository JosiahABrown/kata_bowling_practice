def change_value(value):
    if value == "X" or value == "/":
        return 10
    else:
        return value
    

def bowling_score(rolls):
    frame = rolls.split(' ')
    score = 0
    for i, value in enumerate(frame[0:8]):
        if value == "X":
            score += 10 + change_value(frame[i+1]) + change_value(frame[i+2])
            print(i)
        else:
            pass 
    for i, value in enumerate(frame[8:]):
        if value == "X":
            score += 10 + change_value(frame[i+1]) + change_value(frame[i+1])

            
    
    return score
        
            