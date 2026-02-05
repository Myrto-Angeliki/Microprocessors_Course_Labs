from utils import SortedCircuit, process_circuit_with_input_vector, get_valid_inputs, process_circuit_with_truth_table_vectors

FILE_PATH = "C:\\Users\\user\\Desktop\\git_projects\micropros\\Microprocessors_Course_Labs\\Lab3\\circuit_files\\"
NUM_OF_FILES = 3
OPTIONS = {1:"y_or_n", 2:"signal_probs"}   

def choose_input_method(is_user_input, choice, num_of_inputs, default_value):
    if is_user_input:   return get_valid_inputs(OPTIONS[choice], num_of_inputs, default_value)
    else:               return [default_value for i in range(num_of_inputs)]

def get_user_choice_for_input_method(promt):
    print(promt)
    ans = input().strip().lower()
    return (ans == 'y')


def main():
    print(f"\n \t\t\t~~ Running signal probability computations for {NUM_OF_FILES} circuit files ~~\n")

    circuits = []
    for i in range(1,(NUM_OF_FILES+1)):
        circuits.append(SortedCircuit())

    prompt = f"\n Do you wish to choose the display options for the intermediate signal probabilities of each circuit? (y/n): "
    display_intrmdt_steps = choose_input_method(get_user_choice_for_input_method(prompt), 1, NUM_OF_FILES, False)
        
    for i in range(len(circuits)):
        circuits[i].load_from_file((FILE_PATH+f"circuit_file{i+1}.txt"))
        num_of_tpli = len(circuits[i].top_inputs)
        print(f" ## Signal probabilities computation of circuit{i+1} with {num_of_tpli} top level inputs ##")
        prompt = f"\n Do you wish to enter the signal probabilities for the top level inputs of circuit{i+1} (y/n): "
        input_vector = choose_input_method(get_user_choice_for_input_method(prompt), 2, num_of_tpli, 0.5)
        process_circuit_with_input_vector(circuits[i].elements_table, circuits[i].top_inputs, circuits[i].signals, input_vector, circuits[i].circuit_outputs, display_intrmdt_steps[i])

if __name__ == "__main__":
    main()