import random

def MCpi(a,n):
    n_in_square = 0
    n_in_circle = 0
    c_x = a/2
    c_y = a/2
    r = a/2
    rSquared = r**2

    try:
        for i in range(n):
            x = random.uniform(0.0, a)
            y = random.uniform(0.0, a)
            distanceFromO = (x-c_x)**2+(y-c_y)**2
            
            if (distanceFromO <= rSquared):
                n_in_circle += 1
            n_in_square += 1

        p = 4*(n_in_circle/n_in_square)
        return p

    except ZeroDivisionError as err:
        print(f"Error: {err}")
        return -1.0
    except:
        print("Error: Something went wrong")
        return -1.0

def isGateOutputHigh(gateName, vector):
    if gateName == "AND":
        return (0 not in vector)
    elif gateName == "NAND":
        return (0 in vector)
    elif gateName == "OR":
        return (1 in vector)
    elif gateName == "NOR":
        return (1 not in vector)
    elif gateName == "XOR":
        result = False
        for input in vector:
            if input == 1: result = not result
        return result
    elif gateName == "XNOR":
        result = True
        for input in vector:
            if input == 1: result = not result
        return result
    else:
         return (1 not in vector)
    
def MCGate(gateName, NumOfInputs, n, doSp=0, spList=[]):
    workload = []
    for i in range(n):
        l = []
        for j in range(NumOfInputs):
            if doSp == 0: r = random.randint(0,1)
            else:
                ra = random.uniform(0.0, 1.0)
                r = 0
                if ra < spList[j]: r = 1
            l.append(r)          
        workload.append(l)

    previous_gate_output = 0
    switches_number = 0
    
    for vector in workload:
        new_gate_output = 0
        if isGateOutputHigh(gateName, vector):
                new_gate_output = 1
        if previous_gate_output==new_gate_output:
            continue          
        previous_gate_output = new_gate_output
        switches_number += 1
    try:
        spGate = (switches_number/n)
    except Exception as err:
        print(f"Error: {err}")
        return -1
    return spGate
