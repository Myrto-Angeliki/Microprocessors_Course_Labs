import sys
from utils import mc_gate, mc_pi

MENU_OPTIONS = ["1", "2", "3", "4", "5"]
VALID_GATE_NAMES = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR", "NOT"]

def display_result(mc_op_name, sample_size, gate_name, num_of_inputs, result):
    op = {"mc_pi"    : "Pi",
          "mc_gate"   : f"{gate_name}{num_of_inputs} Switching activity"}
    print(" ---------------------------------------------------------------") 
    print(f" {mc_op_name}: N = {sample_size}, {op[mc_op_name]} = {result: .5f}")
    print(" ---------------------------------------------------------------")  


def call_mc_operation(mc_op_name, sample_size, gate_name, num_of_inputs):
    result = 0
    if mc_op_name == "mc_pi":       result = mc_pi(1, sample_size)
    elif mc_op_name == "mc_gate":   result = mc_gate(gate_name, num_of_inputs, sample_size)
    display_result(mc_op_name, sample_size, gate_name, num_of_inputs, result)
    

def execute_menu_option(mc_op_name, input_sample_size = 0, gate_name="AND", num_of_inputs=2):
    sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]
    if input_sample_size == 0:
        for n in sample_sizes:
            call_mc_operation(mc_op_name, n, gate_name, num_of_inputs)
    else:   call_mc_operation(mc_op_name, input_sample_size, gate_name, num_of_inputs)         


def handle_pos_integer_input(option):
    print(f" Enter the {option}:", end=" ")
    user_input = input().strip()
    if user_input.isnumeric() and user_input != "0":  return int(user_input)
    else: 
        raise Exception("Error: Only a positive integer is allowed as input.")


def handle_gate_name_input():
    print(" Enter gate name:", end=" ")
    gate_name = input().strip().upper()
    if gate_name not in VALID_GATE_NAMES:
        raise Exception(f"Error: The gate name must be one of the following: {VALID_GATE_NAMES}")
    return gate_name


def handle_option_four():
    gate_name = handle_gate_name_input()
    num_of_inputs = 1
    if gate_name != "NOT": num_of_inputs = handle_pos_integer_input("number of inputs")
    sample_size = handle_pos_integer_input("sample size")
    execute_menu_option("mc_gate", sample_size, gate_name, num_of_inputs)


def handle_option_two():
    sample_size = handle_pos_integer_input("sample size")
    execute_menu_option("mc_pi", sample_size)


def handle_menu_option(option): 
    try:
        if   option == "1":   execute_menu_option("mc_pi")
        elif option == "2":   handle_option_two()
        elif option == "3":   execute_menu_option("mc_gate")
        elif option == "4":   handle_option_four()
    except Exception as e: print(e)


def promt_input():
    print("\n Choose an option:", end=" ")
    option = input()
    while option not in MENU_OPTIONS:
        print(f" Please choose an option between 1 and {MENU_OPTIONS[-1]}:", end=" ")
        option = input()
    return option


def display_menu():
    print("\n-------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tMonte Carlo Simulations")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("| (1) Monte Carlo Pi estimation                                    -> sample sizes = [10, 100, 1000, 10000, 100000, 1000000]  |")
    print("| (2) Monte Carlo Pi estimation                                    -> Enter a sample size                                     |")
    print("| (3) Monte Carlo 2 input AND Gate switching activity estimation   -> sample sizes = [10, 100, 1000, 10000, 100000, 1000000]  |")
    print("| (4) Monte Carlo X input Logic Gate switching activity estimation -> Enter the gate name, a value for X, and a sample size   |")
    print("| (5) Exit                                                                                                                    |")
    print("-------------------------------------------------------------------------------------------------------------------------------")


def main(argv):
    display_menu()
    option = promt_input()
    while option != MENU_OPTIONS[-1]:
        handle_menu_option(option)
        display_menu()
        option = promt_input()

if __name__ == "__main__":
    main(sys.argv)