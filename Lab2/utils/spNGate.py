def display_gate_sp(gate_name, inputs_sp, ans):
    opt = "probabilities" if gate_name != "NOT" else "probability"
    if not (type(ans) is list):
        print(f"\n {gate_name} Gate signal probability output for input {opt} {inputs_sp}: {ans: .5f}")
    else:
        for inSp, outSp in zip(inputs_sp, ans):
           print(f"\n {gate_name} Gate signal probability output for input {opt} {inSp}: {outSp: .5f}") 
    print("--------------------------------------------------------------------------------------------")


def display_start(end_string = ""):
    print("\n--------------------------------------------------------------------------------------------")
    print(f" ### Executing signal probability evaluation of {end_string} gate ###")


def get_final_sp(gate_name, sp):
    gates = ["XNOR", "OR", "NAND"]
    if gate_name in gates:   return (1.0-sp)
    else:                    return sp


def get_partial_sp_of_gate(gate_name, sp, input_sp):
    if   gate_name == "AND" or gate_name == "NAND":   return sp*input_sp
    elif gate_name == "OR"  or gate_name == "NOR":    return sp*(1.0-input_sp)
    elif gate_name == "XOR" or gate_name == "XNOR":   return (sp*(1.0-input_sp) + (1.0-sp)*input_sp)


def initialize_sp(gate_name, first_sp):
    if gate_name == "OR" or gate_name == "NOR":   return (1.0 - first_sp)
    else:                                         return first_sp
    

def get_sp_of_gate(inputs_sp, gate_name, display_mode=1):
    if display_mode==1: display_start(f"a {len(inputs_sp)}-input {gate_name}")
    sp = initialize_sp(gate_name, inputs_sp[0])
    for input_sp in inputs_sp[1:]:
        sp = get_partial_sp_of_gate(gate_name, sp, input_sp)
    sp = get_final_sp(gate_name, sp)
    if display_mode==1: display_gate_sp(gate_name, inputs_sp, sp)
    return sp


def handle_NOT_gate(inputs_sp, display_mode=1):
    if display_mode==1: display_start("a NOT")
    if not (type(inputs_sp) is list):
        sp = (1.0 - inputs_sp)
    elif len(inputs_sp) == 1:
        sp = (1.0 - inputs_sp[0])
        inputs_sp = inputs_sp[0]
    else:
        if display_mode==1: print(f"\n Warning: a NOT gate has only one input. {len(inputs_sp)} NOT gates will be created for each input.")
        sp = [(1.0 - sp) for sp in inputs_sp]
    if display_mode==1: display_gate_sp("NOT", inputs_sp, sp)
    return sp
    

def check_num_of_inputs(gate_name, inputs_sp):
    if len(inputs_sp) > 1:
        return True
    else:
        print(f"\n Error: {gate_name} must have at least two inputs.")
        return False


def is_NOT_gate(gate_name):
    if gate_name != "NOT":   return False
    else:                    return True


def check_gate_name(gate_name):
    valid_gate_names = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR", "NOT"]
    if gate_name in valid_gate_names: 
        return True
    else:
        print(f"\n Error: The name of the gate must be one of the following: {valid_gate_names}.")
        return False
    
def evaluate_sp_function(gate_name, inputs_sp, display_mode=1):
    if check_gate_name(gate_name): 
        if not is_NOT_gate(gate_name):
            if check_num_of_inputs(gate_name, inputs_sp):
                return get_sp_of_gate(inputs_sp, gate_name, display_mode)
            else:
                return -1
        else:
            return handle_NOT_gate(inputs_sp, display_mode)
    else:
        return -1