from utils import mc_gate, evaluate_sp_function

CHECK_VALUE = 0.5

def display_switching_activity_results(mc_switching_activities, signal_probabilities, element_table):
    for element in element_table:
        signal_probability = signal_probabilities[element.output]
        esw = 2*signal_probability(1-signal_probability)
        print(f"----------------------------------------------------------------------")
        print(f"Switching activity for {element.element_type} with inputs {element.inputs} and output {element.output}")
        print(f"Monte Carlo switching activity estimation: {mc_switching_activities[element.output]}")
        print(f"Signal probability estimated switching activity: {esw}")
        print(f"----------------------------------------------------------------------")


def compute_switching_acitivity_with_mc(element, signals_table, n):
    element_input_probabilities = [signals_table[input] for input in element.inputs]
    mc_switching_activity = mc_gate(element.element_type, len(element.inputs), n, True, element_input_probabilities)
    return mc_switching_activity


def process(element_table, signals_table):
    for element in element_table:
        element_input_probabilities = [signals_table[input] for input in element.inputs]
        signals_table[element.output] = evaluate_sp_function(element.element_type, element_input_probabilities, False)
    return signals_table

def process_circuit_with_check_value_for_tpl_inputs(element_table, tpl_inputs, signals_table):
    for tpl_input in tpl_inputs:
        signals_table[tpl_input] = 0.5
    return process(element_table, signals_table)


def get_next_value(input_vector, vector_index):
    if vector_index == 0: negate = True
    else:
        negate = True
        for i in range((vector_index)):
            if input_vector[i] == 0:
                negate = False
                break
    if negate: input_vector[vector_index] = 1 - input_vector[vector_index]
    return input_vector


def apply_truth_table_vector_values_for_tpl_inputs(element_table, tpl_inputs, signals_table):
    num_of_inputs  = len(tpl_inputs)
    num_of_vectors = num_of_inputs ** 2
    input_vector = [0 for tpl_input in tpl_inputs] 
    for i in range(num_of_vectors):
        previous_input_vector = input_vector[:]
        for tpl_input, i in zip(tpl_inputs, range(num_of_inputs)):
            signals_table[tpl_input] = input_vector[i]
            input_vector[i] = get_next_value(previous_input_vector, i)
        process(element_table, signals_table)

