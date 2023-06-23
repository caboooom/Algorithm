
def solution(order):
    answer = 0
    n = len(order)

    container = 1
    temp = []
    truck = 0
    
    for box in order:
        if box >= container:
            while True:
                if container == box:
                    truck += 1
                    container += 1
                    break
                else:
                    temp.append(container)
                container += 1
        
        elif len(temp)>0 and temp.pop() == box:
            truck += 1
        else:
            return truck
    
    return truck