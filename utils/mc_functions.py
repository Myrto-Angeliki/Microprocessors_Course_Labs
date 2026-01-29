import random

def mc_pi(a,n):
    n_in_square = 0
    n_in_circle = 0
    c_x = a/2
    c_y = a/2
    r = a/2
    r_squared = r**2
    for i in range(n):
        x = random.uniform(0.0, a)
        y = random.uniform(0.0, a)
        distance_from_center = (x-c_x)**2+(y-c_y)**2
        if (distance_from_center <= r_squared): n_in_circle += 1
        n_in_square += 1
    try:
        p = 4*(n_in_circle/n_in_square)
        return p
    except ZeroDivisionError as err:
        print(f"Error: {err}")
        return -1.0
    except:
        print("Error: Something went wrong")
        return -1.0


def is_gate_output_high(gate_name, vector):
    if   gate_name == "AND":     return (0 not in vector)
    elif gate_name == "NAND":    return (0 in vector)
    elif gate_name == "OR":      return (1 in vector)
    elif gate_name == "NOR":     return (1 not in vector)
    elif gate_name == "XOR":
        result = False
        for input in vector:
            if input == 1: result = not result
        return result
    elif gate_name == "XNOR":
        result = True
        for input in vector:
            if input == 1: result = not result
        return result
    else:   
        return (1 not in vector)

    
def mc_gate(gate_name, num_of_inputs, n, has_input_sps=False, sp_list=[]):
    workload = []
    for i in range(n):
        if gate_name != "NOT":
            input_vector = []
            for j in range(num_of_inputs):
                if has_input_sps: 
                    ra = random.uniform(0.0, 1.0)
                    r = 0
                    if ra < sp_list[j]: r = 1
                else:
                    r = random.randint(0,1)
                input_vector.append(r) 
        else: input_vector = [random.randint(0,1)]  
        workload.append(input_vector)

    if is_gate_output_high(gate_name, workload[0]): previous_gate_output = 1
    else: previous_gate_output = 0
    switches = 0
    for input_vector in workload[1:]:
        new_gate_output = 0
        if is_gate_output_high(gate_name, input_vector):    new_gate_output = 1
        if previous_gate_output == new_gate_output:         continue          
        previous_gate_output = new_gate_output
        switches += 1
    try:
        sp_of_gate = (switches/(n-1))
    except Exception as err:
        print(f"Error: {err}")
        return -1
    return sp_of_gate