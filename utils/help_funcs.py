INPUT_Y_OR_N_ERROR_MSG = (
        " You must enter a sequence of \"y\" and \"n\" (one for each circuit file) seperated by \",\".")

INPUT_PROMPTS = {"signal_probs": (" Enter the signal probabilities of the top level inputs seperated by \",\": "),
                 "y_or_n": " Enter \"y\" or \"n\" seperated by \",\" for each circuit file, if you want its intermediate signal probabilities to be displayed: "}


def handle_pos_integer_input(option, error_msg):
        print(f" Enter the {option}: ", end="")
        user_input = input().strip()
        if user_input.isnumeric() and user_input != "0":  return int(user_input)
        else: 
            raise Exception(f" Error: {error_msg}")

def parse_yes_or_no(input):
    if input == 'y':
        return True
    elif input == 'n':
        return False
    else:
        raise Exception(f"Invalid input {input}.\n"+INPUT_Y_OR_N_ERROR_MSG)

def parse_prob(input):
    prob = float(input)
    if 0.0 <= prob <= 1.0:
        prob = round(prob, 5)
        return prob
    else:
        raise Exception("Expected a value inside the range [0,1]")
    

def parse_input(option, input):
    if option == "signal_probs": 
        return parse_prob(input)
    elif option == "y_or_n":
        return parse_yes_or_no(input.lower())
    else:
        raise Exception(f"{option} is not a valid option")
    

def parse_inputs_from_string(option):
    input_list = input().split(",")
    final_input_list = []
    for inpt in input_list:
        try:
            final_input_list.append(parse_input(option, inpt.strip()))
        except Exception as e:
            print(f" Error: {e}")
            return None
    return final_input_list

def get_inputs(option):
    print(INPUT_PROMPTS[option])
    inputs_list = parse_inputs_from_string(option)
    while not inputs_list:
        print(INPUT_PROMPTS[option])
        inputs_list = parse_inputs_from_string(option)
    return inputs_list

def get_valid_inputs(option, num_of_inputs, default_value):
    inputs_list = get_inputs(option)
    len_of_il = len(inputs_list)
    if len_of_il < num_of_inputs: print(f" Warning: Missing inputs. The rest of the inputs will be set to {default_value}")
    if len_of_il > num_of_inputs: print(f" Warning: Too many inputs. The rest of the inputs will be ignored")
    while len_of_il != num_of_inputs: 
        if len_of_il < num_of_inputs:   inputs_list.append(default_value)
        else:                           inputs_list.pop()
        len_of_il = len(inputs_list)        
    return inputs_list