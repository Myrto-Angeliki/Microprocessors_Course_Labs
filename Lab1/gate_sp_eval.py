import sys
from utils import evaluate_sp_function, get_inputs, Menu

SP_MENU_OPTIONS = ["1", "2", "3"]

class GateSpEval():
    def __init__(self):
        pass

    def execute_default_examples(self):
        gates = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR"]
        for gate_name in gates:
            evaluate_sp_function(gate_name, [0.5, 0.5])
            evaluate_sp_function(gate_name, [0.5, 0.5, 0.5])
        evaluate_sp_function("NOT", 0.5)


    def prompt_gate_name_and_input_sps(self):
        print(" Enter gate name:", end=" ")
        gate_name = input().strip().upper()
        input_sps = get_inputs("signal_probs")
        if input_sps:
            evaluate_sp_function(gate_name, input_sps)


class GateSpEvalMenu(Menu):
    def __init__(self, menu_options):
        super().__init__(menu_options)

    def handle_menu_option(self, option):
        if option == "1":
            GateSpEval().execute_default_examples()
        elif option == "2":
            GateSpEval().prompt_gate_name_and_input_sps()

    def display_menu(self):
        print("\n---------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\tSignal Probability evaluation of a Gate")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("| (1) Execute default examples                                                                                      |")
        print("| (2) Enter the gate name and the signal probabilities of the inputs                                                |")
        print(f"| ({self.menu_options[-1]}) Exit                                                                                                          |")
        print("---------------------------------------------------------------------------------------------------------------------")


def main(argv):
    GateSpEvalMenu(SP_MENU_OPTIONS).start_menu()

if __name__ == "__main__":
    main(sys.argv)