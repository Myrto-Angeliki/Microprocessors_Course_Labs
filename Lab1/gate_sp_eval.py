import sys
from utils import evaluate_sp_function, get_inputs

MENU_OPTIONS = ["1", "2", "3"]

def execute_default_examples():
    gates = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR"]
    for gate_name in gates:
        evaluate_sp_function(gate_name, [0.5, 0.5])
        evaluate_sp_function(gate_name, [0.5, 0.5, 0.5])
    evaluate_sp_function("NOT", 0.5)


def prompt_gate_name_and_input_sps():
    print(" Enter gate name:", end=" ")
    gate_name = input().strip().upper()

    input_sps = get_inputs("signal_probs")
    if input_sps:
        evaluate_sp_function(gate_name, input_sps)


def handle_menu_option(option):
    if option == "1":
        execute_default_examples()
    elif option == "2":
        prompt_gate_name_and_input_sps()


def prompt_input():
    print("\n Choose an option:", end=" ")
    option = input().strip()
    while option not in MENU_OPTIONS:
        print(f" Please choose an option between 1 and {MENU_OPTIONS[-1]}:", end=" ")
        option = input().strip()
    print()
    return option


def display_menu():
    print("\n---------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\tSignal Probability evaluation of a Gate")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("| (1) Execute default examples                                                                                      |")
    print("| (2) Enter the gate name and the signal probabilities of the inputs                                                |")
    print(f"| ({MENU_OPTIONS[-1]}) Exit                                                                                                          |")
    print("---------------------------------------------------------------------------------------------------------------------")


def main(argv):
    display_menu()
    option = prompt_input()
    while option != MENU_OPTIONS[-1]:
        handle_menu_option(option)
        display_menu()
        option = prompt_input()


if __name__ == "__main__":
    main(sys.argv)