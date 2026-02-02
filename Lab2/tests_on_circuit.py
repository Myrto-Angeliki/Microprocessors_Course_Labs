from utils import mc_gate, evaluate_sp_function, Element, CircuitParser

CHECK_VALUE = 0.5

def display_switching_activity_results(mc_switching_activities, signal_probabilities, elements_table, sample_size):
    for element in elements_table:
        signal_probability = signal_probabilities[element.output]
        esw = 2*signal_probability*(1-signal_probability)
        print(f"----------------------------------------------------------------------")
        print(f"Switching activity for {element.element_type} with inputs {element.inputs} and output {element.output}")
        print(f"Monte Carlo switching activity estimation for sample size = {sample_size}: {mc_switching_activities[element.output]}")
        print(f"Signal probability estimated switching activity: {esw}")
        print(f"----------------------------------------------------------------------\n")


def compute_switching_acitivities_with_mc(element_table, signals_table, n):
    mc_switching_activities = {}
    for element in element_table:
        element_input_probabilities = [signals_table[input] for input in element.inputs]
        mc_switching_activity = mc_gate(element.element_type, len(element.inputs), n, True, element_input_probabilities)
        mc_switching_activities[element.output] = mc_switching_activity
    return mc_switching_activities


def display_results_after_process(signals_table, circuit_outs, tpl_inputs, input_vector):
    outputs_signal_probs = [signals_table[output] for output in circuit_outs]
    print(f" Process of circuit complete\n For top level inputs", end="")
    print(f" {tpl_inputs} = {input_vector[::-1]} => {circuit_outs} = {outputs_signal_probs}\n")


def process(elements_table, signals_table, input_vector, circuit_outs, tpl_inputs, display_intermediate_results = False):
    for element in elements_table:
        element_input_probabilities = [signals_table[input] for input in element.inputs]
        signals_table[element.output] = evaluate_sp_function(element.element_type, element_input_probabilities, False)
        if display_intermediate_results: print(f" {element.inputs} = {element_input_probabilities} => {element.output} = {signals_table[element.output]}")
    display_results_after_process(signals_table, circuit_outs, tpl_inputs, input_vector)
    return signals_table


def process_circuit_with_input_vector(elements_table, tpl_inputs, signals_table, input_vector, circuit_outs, display_intermediate_results):
    for tpl_input, vector_input in zip(tpl_inputs, input_vector):
        signals_table[tpl_input] = vector_input
    process(elements_table, signals_table, input_vector, circuit_outs, tpl_inputs, display_intermediate_results)
    print(f" ----------------------------------------------------------------------\n")


def get_next_value(input_vector_original, vector_index):
    input_vector = input_vector_original[:]
    if vector_index == 0: negate = True
    else:
        negate = True
        for i in range(vector_index):
            if input_vector[i] == 0:
                negate = False
                break
    if negate: input_vector[vector_index] = 1 - input_vector[vector_index]
    return input_vector[vector_index]


def process_circuit_with_truth_table_vectors(elements_table, tpl_inputs, signals_table, circuit_outs, display_intermediate_results=False):
    num_of_inputs  = len(tpl_inputs)
    num_of_vectors = 2 ** num_of_inputs
    input_vector = [0 for tpl_input in tpl_inputs] 
    for j in range(num_of_vectors):
        previous_input_vector = input_vector[:]
        for tpl_input, i in zip(tpl_inputs[::-1], range(num_of_inputs)):
            signals_table[tpl_input] = input_vector[i]
            input_vector[i] = get_next_value(previous_input_vector, i)
        process(elements_table, signals_table, previous_input_vector, circuit_outs, tpl_inputs, display_intermediate_results)
    print(f" ----------------------------------------------------------------------\n")
        

def main():
    e1 = Element("AND",['a','b'],'c')
    e2 = Element("NOT",['e'],'f')
    e3 = Element("AND",['c','f'],'d')

    elements_table   = [e1, e2, e3]
    signals_table    = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
    elements_outputs = CircuitParser().get_elements_outputs(elements_table)
    tpl_inputs       = CircuitParser().find_top_inputs(elements_table, elements_outputs)
    elements_inputs  = CircuitParser().get_elements_inputs(elements_table)
    circuit_outputs  = CircuitParser().get_circuit_outputs(elements_outputs, elements_inputs)

    input_vector = [0.5 for input in tpl_inputs]
    process_circuit_with_truth_table_vectors(elements_table, tpl_inputs, signals_table, circuit_outputs)
    process_circuit_with_input_vector(elements_table, tpl_inputs, signals_table, input_vector, circuit_outputs, True)
    mc_sample_size = 200000
    mc_switching_activities = compute_switching_acitivities_with_mc(elements_table, signals_table, mc_sample_size)
    display_switching_activity_results(mc_switching_activities, signals_table, elements_table, mc_sample_size)


if __name__ == "__main__":
    main()